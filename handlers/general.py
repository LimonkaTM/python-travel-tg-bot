from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, FSInputFile

from loader import bot
from keyboards.audio_gid import create_mian_audio_gid_msg_kb
from keyboards.general import create_start_msg_kb


router = Router(name="generalRouter")


@router.callback_query(F.data == "close_msg")
async def close_msg(callback: CallbackQuery, ) -> None:

    '''
    Обработка нажатия на кнопку "Назад" для удаления сообщения
    '''

    await callback.message.delete()


@router.callback_query(F.data == "send_main_msg")
async def send_main_msg(callback: CallbackQuery, ) -> None:

    '''
    Отправляет начальное сообщение
    '''

    await callback.message.delete()

    photo = FSInputFile('assets/img/travel_around_Arkhangelsk.jpg')

    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=photo,
                         reply_markup=create_start_msg_kb())

    return None


@router.callback_query(F.data == "send_audio_gid_msg")
async def send_audio_gid_msg(callback: CallbackQuery, ) -> None:

    '''
    Обработка нажатия на кнопку "Вернуться" для удаления сообщения
    '''

    await callback.message.delete()

    photo = FSInputFile('assets/img/start_audio_gid.jpg')

    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=photo,
                         reply_markup=create_mian_audio_gid_msg_kb())

    return None
