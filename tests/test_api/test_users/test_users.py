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

@pytest.mark.asyncio
async def test_update_existing_user(client):
    """
    Тест: повторная регистрация того же пользователя
    должна обновить данные и вернуть is_new=False
    """

    unique_id = int(time.time() * 1000) + 1 

    response = await client.post(
        "/users/register",
        json={
            "telegram_id": unique_id,
            "username": "test_user",
            "first_name": "Тест"
        }
    )

    data = response.json()

    assert data["is_new"] == True

    response = await client.post(
        "/users/register",
        json={
            "telegram_id": unique_id,
            "username": "Anton",
            "first_name": "Chugur"
        }
    )

    data = response.json()

    assert response.status_code == 201
    assert data["is_new"] == False
    assert data["username"] == "Anton"
    assert data["first_name"] == "Chugur"
    assert data["telegram_id"] == unique_id

#запуск pytest tests/test_api/test_users/test_users.py -v