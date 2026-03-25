from aiogram import Dispatcher
from app.bot.handlers import register_routers

def setup_dispatcher() -> Dispatcher:
    dp = Dispatcher()

    register_routers(dp)

    return dp

dp = setup_dispatcher()