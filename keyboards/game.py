from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from loader import game_data


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


def create_question_kb(question_index: int) -> InlineKeyboardMarkup:

    '''
    Создаёт клавиатуру сообщения игры

    Args:
        question_index (int): индекс вопроса в массиве

    Returns:
        InlineKeyboardMarkup: объект типа InlineKeyboardMarkup
    '''

    keyboard_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    question_answers = game_data[question_index]['answers']

    for question_loop_index, question_answer in enumerate(question_answers):

        keyboard_builder.button(
            text=question_answer,
            callback_data=f'question_answere_index:{question_loop_index}'
        )

    keyboard_builder.button(text="Выйти",
                            callback_data="cancel_state")

    keyboard_builder.adjust(1)

    return keyboard_builder.as_markup()
