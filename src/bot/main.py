import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage

from src.config import TELEGRAM_BOT_TOKEN
from src.bot.middleware.auth import AuthMiddleware
from src.bot.routers import std_r, signup_r


bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


dp.include_routers(std_r, signup_r)

std_r.message.middleware(AuthMiddleware())


commands = []


async def run():
    await bot.set_my_commands(commands=commands)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(run())