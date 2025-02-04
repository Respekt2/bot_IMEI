import asyncio
from aiogram import Bot, Dispatcher
from handlers import router
from bot_IMEI.loader import TOKEN

async def main():
    bot = Bot(token=f"{TOKEN}")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
