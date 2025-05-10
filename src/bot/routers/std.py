from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import httpx

from src.bot.states.auth import AuthStates
from src.utils.password_manager import password_manager
from src.config import API_KEY, BASE_API_URL


std_r = Router()


@std_r.message(Command('start'))
async def start(message: Message, state: FSMContext):

    data = await state.get_data()
    user: dict = data.get('user')

    return message.answer(f'Hi, {user.get("name")}!')
