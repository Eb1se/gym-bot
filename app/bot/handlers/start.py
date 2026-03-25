from aiogram import Router, types
from aiogram.filters import Command
from app.clients.api_client import api_client
import app.bot.messages.start as txt

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    """
    Регистрация пользователя через API
    """
    try:
        telegram_id = message.from_user.id
        username = message.from_user.username
        first_name = message.from_user.first_name

        result = await api_client.register_user(
            telegram_id=telegram_id,
            username=username,
            first_name=first_name
        )

        if result["is_new"]:
            text = txt.welcome_new_user(result["first_name"])
        else:
            text = txt.welcome_back_user(result["first_name"])
        
        await message.answer(text)
    except Exception:
        await message.answer(txt.error_api_unavailable())