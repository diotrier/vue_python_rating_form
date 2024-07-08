import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/test_db"

engine = create_async_engine(DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

@pytest.fixture(scope="module")
async def db_session():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with TestingSessionLocal() as session:
        yield session
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture(scope="module")
async def client(db_session: AsyncSession):
    async def override_get_db():
        yield db_session
    app.dependency_overrides[get_db] = override_get_db
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_create_rating(client: AsyncClient):
    response = await client.post("/ratings/", json={"score": 5})
    assert response.status_code == 200
    data = response.json()
    assert data["score"] == 5

@pytest.mark.asyncio
async def test_read_ratings(client: AsyncClient):
    response = await client.get("/ratings/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
