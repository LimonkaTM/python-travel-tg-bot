from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_help_kb() -> InlineKeyboardMarkup:
    '''
    Создаёт клавиатуру сообщения справки
    '''

    keyboard_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    keyboard_builder.button(
        text='Назад',
        callback_data='send_back_msg:main')

    keyboard_builder.adjust(1)

    return keyboard_builder.as_markup()
