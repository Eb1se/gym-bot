import pytest
import os
from dotenv import load_dotenv
from app.bot.database.models import User
from app.bot.database.base import Base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from httpx import AsyncClient, ASGITransport
from main_api import app 


load_dotenv()

# Берем токен из окружения (из .env файла)
os.environ["BOT_TOKEN"] = os.getenv("BOT_TOKEN", "fallback_token")
os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///./test.db"

print(f"✅ Тестовый режим с токеном: {os.environ['BOT_TOKEN'][:10]}...")

# Тестовая БД (отдельный файл, не трогаем основную)
TEST_DB_URL = "sqlite+aiosqlite:///./test.db"

@pytest.fixture(scope="function")
async def db_session():
    """
    Фикстура, которая создает чистую БД для каждого теста.
    scope="function" — новая БД для каждой тестовой функции.
    """
    # 1. Создаем движок
    engine = create_async_engine(TEST_DB_URL)
    
    # 2. Создаем таблицы (чистая БД)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)   # удаляем старые
        await conn.run_sync(Base.metadata.create_all) # создаем новые
    
    # 3. Создаем фабрику сессий
    async_session = async_sessionmaker(engine, expire_on_commit=False)
    
    # 4. Создаем сессию и отдаем тесту
    async with async_session() as session:
        yield session
    
    # 5. После теста закрываем соединение
    await engine.dispose()

@pytest.fixture
def test_user():
    """Создает тестового пользователя"""
    return User(telegram_id=123, username="test")

@pytest.fixture
async def client():
    """Фикстура для тестирования API"""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client
