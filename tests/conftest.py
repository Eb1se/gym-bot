import pytest
import os
from dotenv import load_dotenv
from app.bot.database.models import User
from httpx import AsyncClient, ASGITransport
from main_api import app 


load_dotenv()

# Берем токен из окружения (из .env файла)
os.environ["BOT_TOKEN"] = os.getenv("BOT_TOKEN", "fallback_token")
os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///./test.db"

print(f"✅ Тестовый режим с токеном: {os.environ['BOT_TOKEN'][:10]}...")

@pytest.fixture
def test_user():
    """Создает тестового пользователя"""
    return User(telegram_id=123, username="test")

@pytest.fixture
async def client():
    """Фикстура для тестирования API"""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client
