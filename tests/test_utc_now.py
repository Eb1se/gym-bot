from datetime import datetime, timezone

"""
TODO:
Сейчас не ругается этот тест
"""

def utc_now():
    """Берем функцию из models.py"""
    return datetime.now(timezone.utc)

def test_utc_now_returns_datetime():
    """Проверяем соответствует ли значение которое вернула функция datetime"""
    result = utc_now()
    assert isinstance(result, datetime)
    print(f"✅ Тип: {type(result)}")

def test_utc_now_naive():
    """Проверяем time"""
    result = utc_now()
    assert result.tzinfo is None
    print(f"✅ Таймзона: {result.tzinfo}")

def test_utc_now_not_none():
    """Проверяем что не None"""
    result = utc_now()
    assert result is not None
    print(f"✅ Время: {result}")

# Запускается: python -m pytest tests/test_utc_now.py -v -s