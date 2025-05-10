import os

from dotenv import load_dotenv

from src.common import root_logger
from src.exceptions import NoneValueInConfig


load_dotenv(override=True)

''' rewrote `os.getenv` method to add one feature: now it will automatically check for `None` (danger!) values'''
def getenv_(key, default=None):
    """Get an environment variable, return None if it doesn't exist.
    The optional second argument can specify an alternate default.
    key, default and the result are str."""

    env_value = os.environ.get(key, default)

    if env_value is None:
        root_logger.critical(f'None value in config file: {key}')

        raise NoneValueInConfig(f'None value in config file: {key}')

    return env_value


BASE_API_URL = 'http://127.0.0.1:8000'

TELEGRAM_BOT_TOKEN: str = getenv_('telegram_bot_token')
API_KEY: str = getenv_('api_key')

# Redis
REDIS_HOST: str = getenv_('redis_host')
REDIS_PORT: int = int(getenv_('redis_port'))
REDIS_DB: int = int(getenv_('redis_db'))
