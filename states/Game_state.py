from aiogram.fsm.state import State, StatesGroup


class GameState(StatesGroup):
    question_index = State()
    game_score = State()
