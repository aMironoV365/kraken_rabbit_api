from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = "sqlite+aiosqlite:///./Kraken_db.db"

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
Base = declarative_base()


async def get_db():
    """
    Зависимость FastAPI: возвращает асинхронную сессию базы данных.
    """
    async with async_session_maker() as session:
        yield session
