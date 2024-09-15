from aiogram.filters.callback_data import CallbackData


class QuestionCallbackFactory(CallbackData, prefix='grade'):
    grade: str
