import os

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession


DATABASE_URL = os.getenv('DATABASE_URL') # postgresql+asyncpg://login:password@db:5432/okkam_data

engine = create_async_engine(
    url=DATABASE_URL
)

async def get_database_session() -> AsyncSession:
    database_session = sessionmaker(
        bind=engine, 
        class_=AsyncSession
    )
    async with database_session() as session:
        yield session
