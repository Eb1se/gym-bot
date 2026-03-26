import pytest
from app.services.user_service import UserService 
from app.api.schemas.user import UserCreate

@pytest.mark.asyncio
async def test_get_user_by_telegram_id(db_session):
    """
    Тест: Поиск юзера по tg_id
    """

    user_data = UserCreate(
        telegram_id = 123456789,
        username="test_user",
        first_name="Тест"
    )

    user, created = await UserService.get_or_create_user(db_session, user_data)
    db_session.commit()

    found = await UserService.get_user_by_telegram_id(db_session, 123456789)

    assert found is not None
    assert found.id == user.id 
    assert found.telegram_id == 123456789
    assert found.username == "test_user"
    assert found.first_name == "Тест"

# Запуск: pytest tests/test_services/test_user_service/test_get_user_by_telegram_id.py -v