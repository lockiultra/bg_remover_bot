import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import image
from config import TG_TOKEN


bot = Bot(token=TG_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

dp.include_router(image.router)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
