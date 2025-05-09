
# here, "fh" stands for "file hanlder"
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "simple": {
            "format": "[%(levelname)s] %(name)s - %(message)s"
        },
        "detailed": {
            "format": "%(asctime)s [%(levelname)s] %(name)s %(funcName)s():%(lineno)d: %(message)s"
        }
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple"
        },
        "root_fh": {
            "class": "logging.FileHandler",
            "filename": f"logs/root.log",
            "level": "DEBUG",
            "formatter": "detailed"
        },
        "bot_fh": {
            "class": "logging.FileHandler",
            "filename": f"logs/bot.log",
            "level": "DEBUG",
            "formatter": "detailed"
        },
    },

    "loggers": {
        "root": {
            "level": "DEBUG",
            "handlers": ["console", "root_fh"],
            "propagate": False
        },
        "bot": {
            "level": "DEBUG",
            "handlers": ["console", "bot_fh"],
            "propagate": False
        }
    }
}
