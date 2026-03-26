import pytest
from app.services.user_service import UserService 
from app.api.schemas.user import UserCreate

@pytest.mark.asyncio
async def test_update_only_username(db_session):
    """
    Проверяем что можно обновить только username, оставив first_name как был.
    """

    user_data = UserCreate(
        telegram_id = 123456789,
        username = "old",
        first_name = "Anton"
    )

    user1, created1 = await UserService.get_or_create_user(db_session, user_data)
    await db_session.commit()

    assert created1 is True
    old_first_name = user1.first_name

    user_data = UserCreate(
        telegram_id = 123456789,
        username = "new",
        first_name = "Anton"
    )

    user2, created2 = await UserService.get_or_create_user(db_session, user_data)
    await db_session.commit()

    assert created2 is False
    assert user2.username == "new"
    assert user2.first_name == old_first_name
    assert user2.first_name == "Anton"

#Запуск: pytest tests/test_services/test_user_service/test_update_only_username.py -v