import asyncio
import logging
from app.bot.core import dp, bot
from app.bot.database.base import create_tables, engine

logging.basicConfig(level=logging.INFO)

async def main():
    logger = logging.getLogger(__name__)

    await create_tables()

    try:
        logger.info("Бот запускается")
        
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        logger.info("Бот остановлен ctrl+c")
    except Exception as e:
        logger.info(f"Произошла ошибка {e}", exc_info=True)
    finally:
        await bot.session.close()
        await engine.dispose()

if __name__ == "__main__":
    asyncio.run(main())
