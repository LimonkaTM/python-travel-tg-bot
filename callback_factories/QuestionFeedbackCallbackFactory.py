from aiogram.filters.callback_data import CallbackData


class QuestionFeedbackCallbackFactory(CallbackData, prefix='grade'):
    grade: str
