from sqlalchemy.ext.asyncio import AsyncSession
from app.bot.database.models import User
from sqlalchemy import select
from typing import Optional, Tuple
from app.api.schemas.user import UserCreate

class UserService:
    """
    Класс с методами для работы с пользователями.
    Все методы статические (@staticmethod), чтобы не создавать экземпляр класса.
    """

    @staticmethod
    async def get_or_create_user(db: AsyncSession, user_data: UserCreate) -> Tuple[User, bool]:
        user = await UserService.get_user_by_telegram_id(db, user_data.telegram_id)

        if user:
            user.username = user_data.username
            user.first_name = user_data.first_name

            await db.commit()
            return user, False

        else:
            user = User(
                telegram_id=user_data.telegram_id,
                username=user_data.username,
                first_name=user_data.first_name
            )
            
            db.add(user)
            await db.commit()
            return user, True


    @staticmethod
    async def get_user_by_telegram_id(db: AsyncSession, telegram_id: int) -> Optional[User]:
        """
        Функция для поиска пользователя в БД
        """
        result = await db.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        user = result.scalar_one_or_none()
        return user