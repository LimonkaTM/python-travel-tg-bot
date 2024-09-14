from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_start_msg_kb() -> InlineKeyboardMarkup:

    '''
    Создаёт клавиатуру стартового сообщения
    '''

    keyboard_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    keyboard_builder.button(
        text='🚶‍♂️ Начать путешествие 🚶‍♂️',
        callback_data='send_tour_msg')
    keyboard_builder.button(
        text='🗺️ Обзор достопримечательностей 🗺️',
        callback_data='send_support_msg')
    keyboard_builder.button(
        text='🎧 Аудио-гид 🎧',
        callback_data='send_about_us_msg')
    keyboard_builder.button(
        text='🎮 Интерактивные игры 🎮',
        callback_data='send_about_us_msg')
    keyboard_builder.button(
        text='📝 Обратная связь 📝',
        callback_data='send_support_msg')
    keyboard_builder.button(
        text='❓ Помощь ❓',
        callback_data='send_support_msg')
    keyboard_builder.button(
        text='Закрыть',
        callback_data='close_msg')

    keyboard_builder.adjust(1)

    return keyboard_builder.as_markup()
