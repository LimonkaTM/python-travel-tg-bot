from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile
from aiogram.fsm.context import FSMContext

from states.game_state import gameState

from loader import bot, game_data

from keyboards.game import create_start_game_kb, create_question_kb


router: Router = Router(name='gameRouter')


@router.callback_query(F.data == 'send_game_msg')
async def send_start_game_msg(callback: CallbackQuery) -> None:
    '''
    Отправляет сообщение c описанием игры
    '''

    photo = InputMediaPhoto(media=FSInputFile(path='assets/img/travel_around_Arkhangelsk.jpg'),
                            caption='<b>Игра-тест</b>\n\nИгра представляет из себя ряд вопросов, на которые Вам предстоит ответить для проверки вашей внимательности.')

    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=photo,
                                 reply_markup=create_start_game_kb())

    return None


@router.callback_query(F.data == 'start_game')
async def send_game_question_msg(callback: CallbackQuery, state: FSMContext) -> None:
    '''
    Отправляет вопрос
    '''

    await callback.message.delete()

    await state.set_state(gameState.question_index)
    await state.update_data(question_index=0)
    await state.update_data(score=0)

    question = game_data[0]['question']

    await bot.send_message(
        chat_id=callback.message.chat.id,
        text=question,
        reply_markup=create_question_kb(0)
    )

    return None


@router.callback_query(QuestionCallbackFactory.filter())
async def process_question_answere(callback: CallbackQuery,
                                   callback_data: QuestionCallbackFactory,
                                   state: FSMContext) -> None:

    '''
    Функция обработки нажатия на кнопки с ответами на вопрос
    '''

    questions = await memory_storage.get_data(bot=bot, key="questions")
    state_data: dict[str, any] = await state.get_data()

    user_score = state_data["score"]
    question_index = state_data["question_index"]

    if callback_data.answer_status == 1:
        user_score += 1

        await state.update_data(score=user_score)

    if question_index < (len(questions) - 1):
        question_index += 1

        question = questions[question_index]

        await state.update_data(question_index=question_index)

        # await callback.message.delete()

        await callback.message.edit_text(
            text=question.text,
            reply_markup=await create_question_kb(question.id))

        await callback.answer()
    else:
        state_data: dict[str, any] = await state.get_data()

        promo = await memory_storage.get_data(bot=bot, key="promocode")

        await callback.message.delete()

        await send_test_results(user_tg_id=callback.message.chat.id,
                                user_score=state_data["score"],
                                question_count=len(questions),
                                promocode_id=promo["id"])
        await state.clear()
        await callback.answer()