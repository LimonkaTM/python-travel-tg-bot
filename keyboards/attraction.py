from aiogram.types import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def photo_navigation_kb(current_index: int) -> InlineKeyboardMarkup:

    '''
    Создаёт клавиатуру "карусель" для просмотра множества фотографий через
    кнопки
    '''

    keyboard_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    keyboard_builder.row(
        InlineKeyboardButton(text='<<',
                             callback_data=f'prev_attraction_photo:{current_index}'
                             ),
        InlineKeyboardButton(text='>>',
                             callback_data=f'next_attraction_photo:{current_index}'
                             )
    )

    keyboard_builder.row(
        InlineKeyboardButton(text='Следующая достопримечательность',
                             callback_data='next_attraction'
                             )
    )

    keyboard_builder.row(
        InlineKeyboardButton(text='На главную',
                             callback_data='close_msg'
                             )
    )

    return keyboard_builder.as_markup()
