from pydantic import BaseModel

class RatingCreate(BaseModel):
    score: int

class Rating(RatingCreate):
    id: int

    class Config:
        orm_mode = True
