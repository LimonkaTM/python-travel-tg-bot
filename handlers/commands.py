from aiogram.dispatcher.router import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

from loader import bot

from keyboards.general import create_start_msg_kb


router: Router = Router(name="commandRouter")


@router.message(Command(commands=["start", "home"]))
async def process_start_cmd(message: Message) -> None:

    '''
    Хендрел /start и /home комманд
    '''

    photo_path = "./assets/img/travel_around_Arkhangelsk.jpg"

    photo = FSInputFile(path=photo_path)

    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo,
                         reply_markup=create_start_msg_kb())
