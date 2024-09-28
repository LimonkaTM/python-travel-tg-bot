from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto
from aiogram.fsm.context import FSMContext

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


@router.callback_query(F.data.startswith('send_back_msg'))
async def send_back_msg(callback: CallbackQuery, ) -> None:
    '''
    Отправляет начальное сообщение
    '''

    message_name = callback.data.split(':')[1]

    match message_name:
        case 'main':
            new_photo = InputMediaPhoto(media=FSInputFile('./assets/img/travel_around_Arkhangelsk.jpg'))

            return await bot.edit_message_media(
                chat_id=callback.message.chat.id,
                message_id=callback.message.message_id,
                media=new_photo,
                reply_markup=create_start_msg_kb()
            )
        case 'audio_gid':
            new_photo = InputMediaPhoto(media=FSInputFile('./assets/img/start_audio_gid.jpg'))

            return await bot.edit_message_media(
                chat_id=callback.message.chat.id,
                message_id=callback.message.message_id,
                media=new_photo,
                reply_markup=create_mian_audio_gid_msg_kb()
            )

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

    new_photo = InputMediaPhoto(media=FSInputFile('./assets/img/start_audio_gid.jpg'))

    return await bot.edit_message_media(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        media=new_photo,
        reply_markup=create_mian_audio_gid_msg_kb()
    )


@router.callback_query(F.data == "cancel_state")
async def cancel_state(callback: CallbackQuery, state: FSMContext) -> None:

    '''
    Обработка нажатия на отмены стейта
    '''

    await callback.message.delete()

    photo_path = "./assets/img/travel_around_Arkhangelsk.jpg"

    photo = FSInputFile(path=photo_path)

    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=photo,
                         reply_markup=create_start_msg_kb())

    await state.clear()

    return None
