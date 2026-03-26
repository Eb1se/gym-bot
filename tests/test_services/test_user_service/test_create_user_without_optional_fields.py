import pytest
from app.services.user_service import UserService 
from app.api.schemas.user import UserCreate

@pytest.mark.asyncio
async def test_create_user_without_optional_fields(db_session):
    """
    Проверяем, что можно создать пользователя только с telegram_id.
    """
    
    user_data = UserCreate(
        telegram_id = 123456789
    )

    user, created = await UserService.get_or_create_user(db_session, user_data)

    assert created is True
    assert user.username is None
    assert user.first_name is None

# Запуск: pytest tests/test_services/test_user_service/test_create_user_without_optional_fields.py -v