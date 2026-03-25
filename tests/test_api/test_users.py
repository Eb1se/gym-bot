import pytest
import time

@pytest.mark.asyncio
async def test_register_new_user(client):
    """Тест регистрации нового пользователя"""

    unique_id = int(time.time() * 1000)

    response = await client.post(
        "/users/register",
        json={
            "telegram_id": unique_id,
            "username": "test_user",
            "first_name": "Тест"
        }
    )
    
    assert response.status_code == 201
    
    data = response.json()

    assert data["telegram_id"] == unique_id
    assert data["username"] == "test_user"
    assert data["first_name"] == "Тест"
    assert data["is_new"] is True
    assert "id" in data
    assert "created_at" in data

#запуск pytest tests/test_api/test_users.py -v