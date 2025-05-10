from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import httpx

from src.bot.states.auth import AuthStates
from src.utils.password_manager import password_manager
from src.config import API_KEY, BASE_API_URL


async def send_data(message: Message, url, data):
    headers = {
        'x-api-key': API_KEY
    }

    async with httpx.AsyncClient(headers=headers) as client:
        response = await client.post(url, headers=[], json=data)

    in_json = response.json()
    return await message.answer(f'{in_json["detail"]}')


signup_r = Router()


@signup_r.message(Command('signup'))
async def signup(message: Message, state: FSMContext):

    await state.set_state(AuthStates.name)

    username = message.from_user.username

    if username:
        return await message.answer(f'let\'s sign you up! enter your username (type "0" to keep "{username}"): ')
    else:
        return await message.answer(f'let\'s sign you up! enter your username:')


@signup_r.message(AuthStates.name)
async def get_name(message: Message, state: FSMContext):
    username = message.text

    if message.from_user.username:
        if username == '0':
            username = message.from_user.username

    await state.update_data(username=username)
    await state.set_state(AuthStates.password)
    await message.answer('now, enter your password. there are no restrictions on the password, but make sure it is secure')


@signup_r.message(AuthStates.password)
async def get_password(message: Message, state: FSMContext):
    password = message.text

    await state.update_data(password=password)
    await message.delete()

    data = await state.get_data()
    username: str = data['username']
    password = data['password']
    telegram_id = message.from_user.id

    try:
        password = password_manager.hash_password(password)
    except AttributeError as er:
        print(er.name)

    await send_data(
        message=message, 
        url=f'{BASE_API_URL}/auth/signup', 
        data={'name': username, 'password': password, 'telegram_id': telegram_id}
    )
    await state.clear()
