from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto

from loader import bot, attraction_data

from keyboards.attraction import photo_navigation_kb


router: Router = Router(name='attractionRouter')


@router.callback_query(F.data.startswith('send_attraction_msg'))
async def process_start_cmd(callback: CallbackQuery) -> None:
    '''
    Хендрел нажатия на кнопку с callback_data == 'send_attraction_msg'
    '''

    await callback.answer()

    photo = InputMediaPhoto(media=FSInputFile(path=attraction_data[0]['photo_paths'][0]),
                            caption=f'<b>{attraction_data[0]["title"]}</b>\n\n{attraction_data[0]["description"]}')

    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=photo,
                                 reply_markup=photo_navigation_kb(currnet_attraction_index=0, current_photo_index=0))

    return None


@router.callback_query(F.data.startswith('prev_attraction_photo') | F.data.startswith('next_attraction_photo'))
async def process_carousel_btns(callback: CallbackQuery) -> None:
    '''
    Смена фотографии в сообщении

    Обрабатывает нажатия на кнопки для смены фотогрфий сообщения
    '''
    current_attraction_index = int(callback.data.split(':')[1])
    current_photo_index = int(callback.data.split(':')[2])

    all_photo_paths = attraction_data[current_attraction_index]['photo_paths']

    if 'prev' in callback.data:
        new_photo_index = (current_photo_index - 1) % len(all_photo_paths)
    else:
        new_photo_index = (current_photo_index + 1) % len(all_photo_paths)

    if new_photo_index == current_photo_index:
        return await callback.answer('')

    new_photo = InputMediaPhoto(media=FSInputFile(all_photo_paths[new_photo_index]),
                                caption=f'<b>{attraction_data[current_attraction_index]["title"]}</b>\n\n{attraction_data[current_attraction_index]["description"]}')

    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=new_photo,
                                 reply_markup=photo_navigation_kb(current_attraction_index, new_photo_index))


@router.callback_query(F.data.startswith('next_attraction'))
async def process_switch_attraction(callback: CallbackQuery) -> None:
    '''
    Смена достопримечательности

    Обрабатывает нажатия на кнопку для смены сообщения с достопримечательностью
    '''

    current_attraction_index = int(callback.data.split(':')[1])

    new_attraction_index = (current_attraction_index + 1)

    if new_attraction_index == len(attraction_data):

        new_photo = InputMediaPhoto(
            media=FSInputFile(attraction_data[0]['photo_paths'][0]),
            caption=f'<b>{attraction_data[0]["title"]}</b>\n\n{attraction_data[0]["description"]}')

        return await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=new_photo,
            reply_markup=photo_navigation_kb(0, 0)
        )

    all_photo_paths = attraction_data[new_attraction_index]['photo_paths']

    new_photo = InputMediaPhoto(media=FSInputFile(all_photo_paths[0]),
                                caption=f'<b>{attraction_data[new_attraction_index]["title"]}</b>\n\n{attraction_data[new_attraction_index]["description"]}')

    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=new_photo,
                                 reply_markup=photo_navigation_kb(new_attraction_index, 0))

    return None
