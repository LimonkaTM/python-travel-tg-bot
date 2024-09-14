from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from config import Config, load_config
from data import get_JSON


config: Config = load_config()

bot: Bot = Bot(token=config.BOT.TOKEN,
               default=DefaultBotProperties(parse_mode='HTML'))
dp: Dispatcher = Dispatcher()
attraction_data: dict = get_JSON(fileName="./database/attraction_data.json", array='attraction')
