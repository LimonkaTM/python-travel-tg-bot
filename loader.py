from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
# from aiogram.fsm.storage.memory import MemoryStorage

from config import Config, load_config


config: Config = load_config()

# memory_storage: MemoryStorage = MemoryStorage()


bot: Bot = Bot(token=config.BOT.TOKEN,
               default=DefaultBotProperties(parse_mode='HTML'))
dp: Dispatcher = Dispatcher()
