from pydantic import BaseModel
from typing import Optional

class ReviewBase(BaseModel):
    comment: str
    rating: int

class ReviewCreate(ReviewBase):
    pass

class ReviewOut(ReviewBase):
    id: int
    book_id: int

    class Config:
        orm_mode = True
