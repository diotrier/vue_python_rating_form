from sqlalchemy import Column, Integer
from .database import Base

class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True)
    score = Column(Integer, index=True)
