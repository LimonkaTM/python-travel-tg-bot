from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_start_game_kb() -> InlineKeyboardMarkup:
    '''
    Создаёт клавиатуру раздела c игрой
    '''

    keyboard_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    keyboard_builder.button(
        text='Играть',
        callback_data='start_game')
    keyboard_builder.button(
        text='Назад',
        callback_data='send_main_msg')

    keyboard_builder.adjust(1)

    return keyboard_builder.as_markup()
