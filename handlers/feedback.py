from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile, Message
from aiogram.fsm.context import FSMContext

from loader import bot, config

from keyboards.feedback import create_feedback_kb, create_grade_kb
from keyboards.general import create_start_msg_kb
from states.feedbackState import feedbackState
from callback_factories.QuestionFeedbackCallbackFactory import QuestionFeedbackCallbackFactory


router: Router = Router(name='feedbackRouter')


@router.callback_query(F.data == 'send_feedback_msg')
async def send_about_tour_msg(callback: CallbackQuery) -> None:
    '''
    Отправляет сообщение c предложением оставить отзыв
    '''

    photo = InputMediaPhoto(media=FSInputFile(path='assets/img/travel_around_Arkhangelsk.jpg'),
                            caption='<b>Оставить отзыв</b>\n\nПутешествинник, напиши отзыв о пройденном туре или о телеграм-боте. Что тебе понравилось? Что можно изменить? Что меньше всего понравилось? Обратная связь для нас очень важна, ведь мы прислушиваемся к предложениям и пожеланиям наших пользователей.')

    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=photo,
                                 reply_markup=create_feedback_kb())

    return None


@router.callback_query(F.data == 'start_feedback_state')
async def send_feedback_tour(callback: CallbackQuery, state: FSMContext) -> None:
    '''
    Обрабатывает нажатие на кнопук "Оставить отзыв" - оценка тура
    '''

    await callback.message.delete()

    await state.set_state(feedbackState.grade_quality_tour)

    await callback.message.answer(text='Поставьте оценку качевства путешествия:',
                                  reply_markup=create_grade_kb())
    await callback.answer()


@router.callback_query(feedbackState.grade_quality_tour, QuestionFeedbackCallbackFactory.filter())
async def send_feedback_bot(callback: CallbackQuery, callback_data: QuestionFeedbackCallbackFactory, state: FSMContext) -> None:
    '''
    Функция обработки нажатия на кнопки с ответами на вопрос о качестве тура
    '''
    answere_grade = callback_data.grade

    await state.update_data(grade_quality_tour=answere_grade)

    await bot.edit_message_text(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        text='Оцените удобство и работу с ботом:',
        reply_markup=create_grade_kb()
    )

    await state.set_state(feedbackState.grade_quality_bot)

    return None


@router.callback_query(feedbackState.grade_quality_bot, QuestionFeedbackCallbackFactory.filter())
async def send_feedback_comment(callback: CallbackQuery, callback_data: QuestionFeedbackCallbackFactory, state: FSMContext) -> None:
    '''
    Функция обработки нажатия на кнопки с ответами на вопрос работы с ботом
    '''

    answere_grade = callback_data.grade

    await state.update_data(grade_quality_bot=answere_grade)
    await state.update_data(message_delete_chat_id=callback.message.chat.id)
    await state.update_data(message_delete_id=callback.message.message_id)

    await bot.edit_message_text(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        text='Добавьте комментарий к вашему отзыву:'
    )

    await state.set_state(feedbackState.comment)

    return None


@router.message(feedbackState.comment)
async def send_result_comment(message: Message, state: FSMContext) -> None:
    '''
    Функция обработки нажатия на кнопку с отправкой комментария
    '''

    await state.update_data(comment=message.text)

    state_data: dict[str, any] = await state.get_data()

    for admin_id in config.BOT.ADMIN_ID:
        await bot.send_message(
            chat_id=admin_id,
            text=f'ID пользователя: {message.chat.id}\nОценка тура: {state_data["grade_quality_tour"]}\nОценка бота: {state_data["grade_quality_bot"]}\nКоментарий:\n{state_data["comment"]}\n'
        )

    await message.delete()
    await bot.delete_message(
        chat_id=state_data['message_delete_chat_id'],
        message_id=state_data['message_delete_id']
    )

    photo = FSInputFile('assets/img/travel_around_Arkhangelsk.jpg')

    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo,
                         reply_markup=create_start_msg_kb())

    await state.clear()

    return None
