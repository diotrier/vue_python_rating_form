
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud, models, schemas
from .database import engine, get_db

from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ratings/", response_model=schemas.Rating)
async def create_rating(rating: schemas.RatingCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_rating(db=db, rating=rating)

@app.get("/ratings/", response_model=list[schemas.Rating])
async def read_ratings(db: AsyncSession = Depends(get_db)):
    return await crud.get_ratings(db=db)