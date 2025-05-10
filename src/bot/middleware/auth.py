from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.filters import Command
from typing import Callable, Dict, Any, Awaitable
from aiogram.fsm.context import FSMContext

from src.cache.redis_manager import redis_manager


class AuthMiddleware(BaseMiddleware):
    '''
    checks user's authentications status.
    '''

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        
        user_tg_id = event.from_user.id

        all_the_users = [v.decode("utf-8") for v in await redis_manager.keys('*')]
        
        if not (f'{user_tg_id}' in all_the_users):
            return event.answer('you are not authenticated. enter /signup to create a new account')

        # add user to state
        state: FSMContext = data.get('state')
        decoded_user = [v.decode("utf-8") for v in await redis_manager.lrange(user_tg_id, 0, -1)]
        await state.update_data(user={
            'name': decoded_user[0]
        })

        return await handler(event, data)    
