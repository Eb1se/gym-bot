from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

from app.bot.core.config import DATABASE_URL

Base = declarative_base()

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

async def create_tables():
    """"Создает все таблицы в БД"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print(f"✅ Таблицы созданы в: {DATABASE_URL}")

# async def drop_tables():
#     """Удаляет все таблицы (только для разработки!)"""
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#     print("⚠️ Все таблицы удалены")