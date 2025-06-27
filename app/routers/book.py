from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models.book import Book
from app.schemas.book import BookCreate, BookOut
from app.services.cache import get_books_cache, set_books_cache, r  # Redis integration
from app.db.database import get_db


router = APIRouter()



@router.get("/books", response_model=List[BookOut])
def get_books(db: Session = Depends(get_db)):
    try:
        cached_books = get_books_cache()
        if cached_books:
            return cached_books
    except Exception as e:
        print(f"[Redis] Cache read failed: {e}")

    books = db.query(Book).all()
    book_out = [BookOut.from_orm(book).dict() for book in books]

    try:
        set_books_cache(book_out)
    except Exception as e:
        print(f"[Redis] Cache write failed: {e}")

    return book_out

@router.post("/books", response_model=BookOut, status_code=201)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    try:
        r.delete("books")  # Invalidate cache
    except Exception as e:
        print(f"[Redis] Cache invalidation failed: {e}")

    return db_book
