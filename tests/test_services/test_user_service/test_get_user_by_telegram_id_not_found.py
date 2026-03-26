import pytest
from app.services.user_service import UserService 

@pytest.mark.asyncio
async def test_get_user_by_telegram_id_not_found(db_session):
    """
    Проверяем, если пользователя нет, значит возвращаем None
    """
    found = await UserService.get_user_by_telegram_id(db_session, 999999999)

    assert found is None

# Запуск: pytest tests/test_services/test_user_service/test_get_user_by_telegram_id_not_found.py -v