from aiogram.fsm.state import State, StatesGroup


class gameState(StatesGroup):
    question_index = State()
    game_score = State()
