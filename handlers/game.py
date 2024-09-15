from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile

from loader import bot

from keyboards.game import create_start_game_kb


router: Router = Router(name='gameRouter')


@router.callback_query(F.data == 'send_game_msg')
async def send_start_game_msg(callback: CallbackQuery) -> None:
    '''
    Отправляет сообщение c описанием игры
    '''

    photo = InputMediaPhoto(media=FSInputFile(path='assets/img/travel_around_Arkhangelsk.jpg'),
                            caption='<b>Игра-тест</b>\n\nИгра представляет из себя ряд вопросов, на которые Вам предстоит ответить для проверки вашей внимательности.')

    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=photo,
                                 reply_markup=create_start_game_kb())

    return None
