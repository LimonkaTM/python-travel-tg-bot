from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto

from loader import bot, attraction_data

from keyboards.attraction import photo_navigation_kb


router: Router = Router(name='attractionRouter')

attractions_JSON: dict = attraction_data


@router.callback_query(F.data == 'send_attraction_msg')
async def process_start_cmd(callback: CallbackQuery) -> None:
    '''
    Хендрел нажатия на кнопку с callback_data == 'send_attraction_msg'
    '''
    
    await callback.answer()

    photo = FSInputFile(path=attraction_data['Rezitsky_square']['photo_paths'][0])

    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=photo,
                         caption=f'<b>{attraction_data["Rezitsky_square"]["title"]}</b>\n\n{attraction_data["Rezitsky_square"]["description"]}',
                         reply_markup=photo_navigation_kb(0))

    return None


@router.callback_query(F.data.startswith('prev_attraction_photo') | F.data.startswith('next_attraction_photo'))
async def process_carousel_btns(callback: CallbackQuery) -> None:
    '''
    Смена фотографии в сообщении

    Обрабатывает нажатия на кнопки для смены фотогрфий сообщения
    '''

    currents_photo_index = int(callback.data.split(':')[1])
    all_photo_paths = attraction_data['Rezitsky_square']['photo_paths']

    print(callback.data.split(':')[0])

    if 'prev' in callback.data:
        new_index = (currents_photo_index - 1) % len(all_photo_paths)
    else:
        new_index = (currents_photo_index + 1) % len(all_photo_paths)

    new_photo = InputMediaPhoto(media=FSInputFile(all_photo_paths[new_index]),
                                caption=f'<b>{attraction_data["Rezitsky_square"]["title"]}</b>\n\n{attraction_data["Rezitsky_square"]["description"]}')

    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=new_photo,
                                 reply_markup=photo_navigation_kb(new_index))
