from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile

from loader import bot

from keyboards.about import create_about_kb


router: Router = Router(name='aboutRouter')


@router.callback_query(F.data == 'send_about_tour_msg')
async def send_about_tour_msg(callback: CallbackQuery) -> None:
    '''
    Отправляет сообщение с описанием тура
    '''

    photo = InputMediaPhoto(media=FSInputFile(path='assets/img/travel_around_Arkhangelsk.jpg'),
                            caption='<b>Описание путешествия по Архангельску</b>\n\nЧто-то длфоывлда лдфо офыво длод фыдво длдфоы длыва длофыво двыа')

    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=photo,
                                 reply_markup=create_about_kb())

    return None
