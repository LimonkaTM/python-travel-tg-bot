from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_feedback_kb() -> InlineKeyboardMarkup:
    '''
    Создаёт клавиатуру сообщения обратной связи
    '''

    keyboard_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    keyboard_builder.button(
        text='Написать отзыв',
        callback_data='start_feedback_state')
    keyboard_builder.button(
        text='Назад',
        callback_data='send_back_msg:main')

    keyboard_builder.adjust(1)

    return keyboard_builder.as_markup()


def create_back_feedback_kb() -> InlineKeyboardMarkup:
    '''
    Создаёт возврата к предыдущему стейту
    '''

    keyboard_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    keyboard_builder.button(
        text='Назад',
        callback_data='back_to_prev_state')

    keyboard_builder.adjust(1)

    return keyboard_builder.as_markup()


def create_cancel_feedback_kb() -> InlineKeyboardMarkup:
    '''
    Создаёт клавиатуру отмены отзыва
    '''

    keyboard_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    keyboard_builder.button(
        text='Отменить',
        callback_data='cancel_state')

    keyboard_builder.adjust(1)

    return keyboard_builder.as_markup()


def create_grade_kb() -> InlineKeyboardMarkup:
    '''
    Создаёт клавиатуру с выбором оценки
    '''

    keyboard_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    keyboard_builder.button(
        text='⭐️⭐️⭐️⭐️⭐️',
        callback_data='grade:5')
    keyboard_builder.button(
        text='⭐️⭐️⭐️⭐️',
        callback_data='grade:4')
    keyboard_builder.button(
        text='⭐️⭐️⭐️',
        callback_data='grade:3')
    keyboard_builder.button(
        text='⭐️⭐️',
        callback_data='grade:2')
    keyboard_builder.button(
        text='⭐️',
        callback_data='grade:1')
    keyboard_builder.button(
        text='Отменить',
        callback_data='cancel_state')

    keyboard_builder.adjust(1)

    return keyboard_builder.as_markup()
