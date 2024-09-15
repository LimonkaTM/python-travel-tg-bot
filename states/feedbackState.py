from aiogram.fsm.state import State, StatesGroup


class feedbackState(StatesGroup):
    grade_quality_tour = State()
    grade_quality_bot = State()
    comment = State()
    message_delete_chat_id = State()
    message_delete_id = State()
