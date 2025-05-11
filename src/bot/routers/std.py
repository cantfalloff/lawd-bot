from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


std_r = Router()


@std_r.message(Command('start'))
async def start(message: Message, state: FSMContext):

    data = await state.get_data()
    user: dict = data.get('user')

    return message.answer(f'Hi, {user.get("name")}!')
