import pytest
import os
from dotenv import load_dotenv

load_dotenv()

# Берем токен из окружения (из .env файла)
os.environ["BOT_TOKEN"] = os.getenv("BOT_TOKEN", "fallback_token")
os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///./test.db"

print(f"✅ Тестовый режим с токеном: {os.environ['BOT_TOKEN'][:10]}...")

@pytest.fixture
def test_user():
    """Создает тестового пользователя"""
    from app.database.models import User
    return User(telegram_id=123, username="test")