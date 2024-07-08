from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine

# engine = create_engine("postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase")

DATABASE_URL = "postgresql+asyncpg://user:password@localhost:8000/mydatabase"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
Base = declarative_base()

async def get_db():
    async with SessionLocal() as session:
        yield session
