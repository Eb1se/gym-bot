import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError(
        "ТОКЕН БОТА НЕ НАЙДЕН!\n"
        "Создайте файл .env с содержимым:\n"
        "BOT_TOKEN=ваш_токен_от_BotFather"
    )

print("Токен бота успешно загружен")

ROOT_DIR = Path(__file__).parent.parent
DEFAULT_DB_URL = f"sqlite+aiosqlite:///{ROOT_DIR}/gym_bot.db"

DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_DB_URL)

print("✅Конфигурация успешно загружена")
