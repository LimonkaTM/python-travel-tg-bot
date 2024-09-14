from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_mian_audio_gid_msg_kb() -> InlineKeyboardMarkup:

    '''
    Создаёт клавиатуру сообщения с аудио-гидом
    '''

    keyboard_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    keyboard_builder.button(
        text='🎧 Начать аудио-экскурсию 🎧',
        callback_data='start_audio_gid')
    keyboard_builder.button(
        text='Список достопремечательностей',
        callback_data='send_list_attraction_msg')
    keyboard_builder.button(
        text='Назад',
        callback_data='back_to_main_msg')

    keyboard_builder.adjust(1)

    return keyboard_builder.as_markup()
