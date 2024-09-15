from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from config import Config, load_config
from data import get_JSON


config: Config = load_config()

memory_storage: MemoryStorage = MemoryStorage()

bot: Bot = Bot(token=config.BOT.TOKEN,
               default=DefaultBotProperties(parse_mode='HTML'))
dp: Dispatcher = Dispatcher(storage=memory_storage)
attraction_data: dict = get_JSON(fileName="./database/data.json", array='attraction')
