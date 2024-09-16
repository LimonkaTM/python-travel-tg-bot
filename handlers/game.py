from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile
from aiogram.fsm.context import FSMContext

from callback_factories.QuestionGameCallbackFactory import QuestionGameCallbackFactory
from states.Game_state import GameState

from loader import bot, game_data

from keyboards.game import create_start_game_kb, create_question_kb
from keyboards.help import create_help_kb

from utils.game import calc_percent_true_answers, define_type_game_result

router: Router = Router(name='gameRouter')


@router.callback_query(F.data == 'send_game_msg')
async def send_start_game_msg(callback: CallbackQuery) -> None:
    '''
    Отправляет сообщение c описанием игры
    '''

    photo = InputMediaPhoto(media=FSInputFile(path='assets/img/game.jpg'),
                            caption='🎮 <b>Игра-викторина</b> 🎮\n\nИгра-викторина представляет из себя небольшой тест на знание информации о достопримечательностях Архангельской области.\n\nВ результате прохождения теста вам будет присвоено звание.\n\nДля того чтобы начать нажмите на кнопку "Играть".\n\nP.S. <i>Стань легендарным покорителем земель, я верю в тебя!</i>')

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

    await state.set_state(GameState.question_index)
    await state.update_data(question_index=0)
    await state.update_data(score=0)

    question = game_data[0]['question']

    await bot.send_message(
        chat_id=callback.message.chat.id,
        text=question,
        reply_markup=create_question_kb(0)
    )

    return None


@router.callback_query(GameState.question_index, QuestionGameCallbackFactory.filter())
async def process_question_answere(callback: CallbackQuery,
                                   callback_data: QuestionGameCallbackFactory,
                                   state: FSMContext) -> None:
    '''
    Функция обработки нажатия на кнопки с ответами на вопрос
    '''
    state_data: dict[str, any] = await state.get_data()

    question_index = state_data["question_index"]
    user_score = state_data["score"]

    true_answer_index = game_data[question_index]['true_answer_index']

    if true_answer_index == callback_data.question_index:
        user_score += 1

        await state.update_data(score=user_score)

    if question_index < (len(game_data) - 1):
        question_index += 1

        question = game_data[question_index]

        await state.update_data(question_index=question_index)

        # await callback.message.delete()

        await callback.message.edit_text(
            text=question['question'],
            reply_markup=create_question_kb(question_index))

        await callback.answer()
    else:
        state_data: dict[str, any] = await state.get_data()

        await callback.message.delete()

        await send_game_results(chat_id=callback.message.chat.id, score=state_data["score"])

        await state.clear()

        await callback.answer()


async def send_game_results(chat_id: int, score: int) -> None:
    '''
    Функция отправки сообщения с результатом игры
    '''

    question_count = len(game_data)

    match define_type_game_result(calc_percent_true_answers(score, question_count)):
        case 'pro':
            message_text = (f"🎉 <b>Поздравляем</b> 🎉\nВы дошли до конца и отлично прошил тест. Как насчёт поменять в университете на туризм?"
                            f'\n\n<b>Ваше звание:</b> профессиональный гид'
                            f"\n\n<b>Ваш результат:</b> {score}/"
                            f"{question_count}\n\n")

            photo_path = "assets/img/pro.jpg"

            photo = FSInputFile(path=photo_path)

            await bot.send_photo(chat_id=chat_id,
                                 photo=photo,
                                 caption=message_text,
                                 reply_markup=create_help_kb())
        case 'middle':
            message_text = (f"🎉 <b>Поздравляем</b> 🎉\nВы дошли до конца и хорошо прошли тест. Вы точно не заблудитесь и сможете смело ориентироваться на местности."
                            f'\n\n<b>Ваше звание:</b> путешественник'
                            f"\n\n<b>Ваш результат:</b> {score}/"
                            f"{question_count}\n\n")

            photo_path = "assets/img/middle.jpg"

            photo = FSInputFile(path=photo_path)

            await bot.send_photo(chat_id=chat_id,
                                 photo=photo,
                                 caption=message_text,
                                 reply_markup=create_help_kb())
        case 'junior':
            message_text = (f"🎉 <b>Поздравляем!</b> 🎉\nВы дошли до конца и почти успешно прошли тест, но к сожалению, вы встали сегодня не стой ноги."
                            f'\n\n<b>Ваше звание:</b> зевака'
                            f"\n\n<b>Ваш результат:</b> {score}/{question_count}"
                            f"\n\n")

            photo_path = "assets/img/junior.jpg"

            photo = FSInputFile(path=photo_path)

            await bot.send_photo(chat_id=chat_id,
                                 photo=photo,
                                 caption=message_text,
                                 reply_markup=create_help_kb())
