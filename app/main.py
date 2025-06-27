from fastapi import FastAPI
from app.routers import book, review

app = FastAPI(title="Book Review Service")

app.include_router(book.router)
app.include_router(review.router)
