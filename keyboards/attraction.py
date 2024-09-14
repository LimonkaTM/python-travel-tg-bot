from aiogram.types import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def photo_navigation_kb() -> InlineKeyboardMarkup:

    '''
    Создаёт клавиатуру "карусель" для просмотра множества фотографий через
    кнопки
    '''

    keyboard_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    keyboard_builder.row(
        InlineKeyboardButton(text='<<',
                             callback_data='prev_attraction_photo'
                             ),
        InlineKeyboardButton(text='>>',
                             callback_data='next_attraction_photo'
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
