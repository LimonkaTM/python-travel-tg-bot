from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


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
        callback_data='send_main_msg')

    keyboard_builder.adjust(1)

    return keyboard_builder.as_markup()


def create_attraction_audio_gid_kb(currnet_audio_gid_index: int) -> InlineKeyboardMarkup:

    '''
    Создаёт клавиатуру "карусель" для просмотра множества фотографий через
    кнопки
    '''

    keyboard_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    keyboard_builder.row(
        InlineKeyboardButton(
            text='<<',
            callback_data=f'prev_audio_gid_attraction:{currnet_audio_gid_index}'
        ),
        InlineKeyboardButton(
            text='>>',
            callback_data=f'next_audio_gid_attraction:{currnet_audio_gid_index}'
        )
    )

    keyboard_builder.row(
        InlineKeyboardButton(
            text='Вернутся',
            callback_data='send_audio_gid_msg'
        )
    )

    return keyboard_builder.as_markup()
