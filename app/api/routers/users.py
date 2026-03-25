from fastapi import APIRouter, Depends, status
from app.api.schemas.user import UserCreate, UserResponse
from app.api.dependencies import get_db
from app.services.user_service import UserService
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/users", tags=["users"])
@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db)
)-> UserResponse:
    """
    Регистрация нового пользователя.

    -Если пользователь с таким telegram_id уже есть - обновляем данные
    -Если нет - создаем нового
    """
    user, created = await UserService.get_or_create_user(db, user_data)

    return UserResponse(
        id = user.id,
        telegram_id=user.telegram_id,
        username=user.username,
        first_name=user.first_name,
        created_at=user.created_at,
        is_new=created
    )
    
    