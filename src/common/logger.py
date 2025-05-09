import logging
import logging.config

from .logging_config import LOGGING_CONFIG


logging.config.dictConfig(LOGGING_CONFIG)

root_logger = logging.getLogger('root')

bot_logger = logging.getLogger('bot')
