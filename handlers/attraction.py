from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, FSInputFile

from loader import bot

from keyboards.attraction import photo_navigation_kb


router: Router = Router(name='attractionRouter')

photo_paths = ['./assets/img/Rezitsky_square.jpg']


@router.callback_query(F.data == 'send_attraction_msg')
async def process_start_cmd(callback: CallbackQuery) -> None:

    '''
    Хендрел нажатия на кнопку с callback_data == 'send_attraction_msg'
    '''
    await callback.answer()

    photo = FSInputFile(path=photo_paths[0])

    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=photo,
                         caption="asdasd",
                         reply_markup=photo_navigation_kb())

    return None
