from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto, InputMediaAudio

from loader import bot, attraction_data

from keyboards.audio_gid import create_attraction_audio_gid_kb, create_list_attraction_kb


router: Router = Router(name='audioGidRouter')


@router.callback_query(F.data == 'start_audio_gid')
async def process_start_cmd(callback: CallbackQuery) -> None:
    '''
    Хендрел нажатия на кнопку начала уадио-экскурсии
    '''

    print(attraction_data[0]['audio_path'])

    await bot.delete_message(chat_id=callback.message.chat.id,
                             message_id=callback.message.message_id)

    audio = FSInputFile(path=attraction_data[0]['audio_path'])

    await bot.send_audio(chat_id=callback.message.chat.id,
                         audio=audio,
                         caption=f'<b>{attraction_data[0]["title"]}</b>\n\n{attraction_data[0]["audio_gid_description"]}',
                         reply_markup=create_attraction_audio_gid_kb(0))

    return None


@router.callback_query(F.data.startswith('prev_audio_gid_attraction') | F.data.startswith('next_audio_gid_attraction'))
async def process_carousel_btns(callback: CallbackQuery) -> None:
    '''
    Смена аудио-сообщения гида
    '''
    current_attraction_index = int(callback.data.split(':')[1])

    if 'prev' in callback.data:
        new_attraction_index = (current_attraction_index - 1) % len(attraction_data)
    else:
        new_attraction_index = (current_attraction_index + 1) % len(attraction_data)

    if new_attraction_index == current_attraction_index:
        return await callback.answer('')

    new_audio = InputMediaAudio(media=FSInputFile(attraction_data[new_attraction_index]['audio_path']),
                                caption=f'<b>{attraction_data[current_attraction_index]["title"]}</b>\n\n{attraction_data[current_attraction_index]["description"]}')

    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=new_audio,
                                 reply_markup=create_attraction_audio_gid_kb(new_attraction_index))

    return None


@router.callback_query(F.data == 'send_list_attraction_msg')
async def send_list_attractions_msg(callback: CallbackQuery) -> None:
    '''
    Отправляет список достопримечательностей для открытия аудио
    '''

    photo = InputMediaPhoto(media=FSInputFile('assets/img/travel_around_Arkhangelsk.jpg'),
                            caption='<b>Выберите достопримечательность чтобы послушать аудио-гид:</b>')

    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=photo,
                                 reply_markup=create_list_attraction_kb())

    return None


@router.callback_query(F.data.startswith('send_audio_gid_msg'))
async def send_audio_gid_msg(callback: CallbackQuery) -> None:
    '''
    Отправляет аудио-сообщение выбранной достопримечательности
    '''
    current_attraction_index = int(callback.data.split(':')[1])

    # if 'prev' in callback.data:
    #     new_attraction_index = (current_attraction_index - 1) % len(attraction_data)
    # else:
    #     new_attraction_index = (current_attraction_index + 1) % len(attraction_data)

    # if new_attraction_index == current_attraction_index:
    #     return await callback.answer('')

    await callback.message.delete()

    audio = FSInputFile(attraction_data[current_attraction_index]['audio_path'])

    await bot.send_audio(chat_id=callback.message.chat.id,
                         audio=audio,
                         caption=f'<b>{attraction_data[current_attraction_index]["title"]}</b>\n\n{attraction_data[current_attraction_index]["description"]}',
                         reply_markup=create_attraction_audio_gid_kb(current_attraction_index))

    return None
