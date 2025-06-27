from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models.book import Book
from app.models.review import Review
from app.schemas.review import ReviewCreate, ReviewOut
from app.db.database import get_db


router = APIRouter()



@router.get("/books/{book_id}/reviews", response_model=List[ReviewOut])
def get_reviews(book_id: int, db: Session = Depends(get_db)):
    return db.query(Review).filter(Review.book_id == book_id).all()

@router.post("/books/{book_id}/reviews", response_model=ReviewOut, status_code=201)
def create_review(book_id: int, review: ReviewCreate, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db_review = Review(**review.dict(), book_id=book_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review
