# app/database/db_init.py
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.config import settings

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False,
)

async_session_factory = async_sessionmaker(async_engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

metadata = Base.metadata

async def get_session() -> AsyncSession:
    async with async_session_factory() as session:
        yield session
