from aiogram.filters.callback_data import CallbackData


class QuestionGameCallbackFactory(CallbackData, prefix='question_answere_index'):
    question_index: int
