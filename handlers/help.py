from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile

from loader import bot

from keyboards.help import create_help_kb


router: Router = Router(name='helpRouter')


@router.callback_query(F.data == 'send_help_msg')
async def send_help_msg(callback: CallbackQuery) -> None:
    '''
    Отправляет сообщение справки пользователя
    '''

    photo = InputMediaPhoto(media=FSInputFile(path='assets/img/travel_around_Arkhangelsk.jpg'),
                            caption='<b>Справка пользователя</b>\n\nЧто-то длфоывлда лдфо офыво длод фыдво длдфоы длыва длофыво двыа')

    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=photo,
                                 reply_markup=create_help_kb())

    return None
