from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas

async def create_rating(db: AsyncSession, rating: schemas.RatingCreate):
    db_rating = models.Rating(score=rating.score)
    db.add(db_rating)
    await db.commit()
    await db.refresh(db_rating)
    return db_rating

async def get_ratings(db: AsyncSession):
    result = await db.execute(select(models.Rating))
    return result.scalars().all()
