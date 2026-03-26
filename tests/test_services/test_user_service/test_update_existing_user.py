import pytest
from app.services.user_service import UserService
from app.api.schemas.user import UserCreate

@pytest.mark.asyncio
async def test_update_existing_user(db_session):
    """
    Тест: обновление существующего пользователя.
    Проверяем что данные обновляются, а created=False
    """

    user_data1 = UserCreate(
        telegram_id = 123456789,
        username = "test_user",
        first_name = "Тест"
    )

    user1, created1 = await UserService.get_or_create_user(db_session, user_data1)
    await db_session.commit()

    first_user_id = user1.id

    user_data2 = UserCreate(
        telegram_id = 123456789,
        username = "Anton",
        first_name = "Chugur"
    )

    user2, created2 = await UserService.get_or_create_user(db_session, user_data2)
    await db_session.commit()

    assert created2 is False
    assert user2.id == first_user_id
    assert user2.username == "Anton"
    assert user2.first_name == "Chugur"

# Запуск pytest tests/test_services/test_user_service/test_update_existing_user.py -v