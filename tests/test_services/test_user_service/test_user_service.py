import pytest
from app.services.user_service import UserService
from app.api.schemas.user import UserCreate

@pytest.mark.asyncio
async def test_create_new_user(db_session):
    """
    Создание нового пользователя.
    Проверяем что пользователь создается с правильными данными.
    """

    user_data = UserCreate(
        telegram_id=123456789,
        username="test_user",
        first_name="Тест"
    )

    user, created = await UserService.get_or_create_user(db_session, user_data)
    await db_session.commit()

    assert user is not None
    assert created is True
    assert user.telegram_id == 123456789
    assert user.username == "test_user"
    assert user.first_name == "Тест"
    assert user.id is not None

# Запуск: pytest tests/test_services/test_user_service/test_user_service.py -v