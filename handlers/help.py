from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile

from loader import bot

from keyboards.help import create_help_kb


router: Router = Router(name='helpRouter')


@router.callback_query(F.data == 'send_help_msg')
async def send_help_msg(callback: CallbackQuery) -> None:
    '''
    Отправляет сообщение справки пользователя
    '''

    photo = InputMediaPhoto(media=FSInputFile(path='assets/img/help.jpg'),
                            caption='❕ <b>Справка пользователя | FAQ</b> ❕\n\n<b>Справка пользователя</b>\nБот имеет лишь одну команду: /start - запуск бота / отправка начального сообщения для дальнейшего взаимодействия.\n\nБольшая часть взаимодействия с ботом реализована через кнопки, прикреплённые к сообщениям, если по каккой-то причине у сообщения нет кнопок - перезапустите бота.\n\n❔ <b>FAQ</b> ❔\n1. <b>Что делать если бот не реагирует на любые действия?</b>\n<i>Это значит, что по каким-то причинам бот не работате, скорее всего ведутся серверные работы.</i>\n\n2. <b>Что делать если не загружаются фотографии/аудио?</b>\n<i>Проблема может быть связана с несатбильным интернет-соединением или с проблемами работы сервиса Telegram. Проверьте ваше интернет-соединение, настройки Telegram.</i>\n\n3. <b>Что делать если бот долго обрабатывает нажатия на кнопки?</b>\n<i>Это означает, что сервер, обрабатывающий запросы перегружен, имеет нестабильное интернет-соединение или какие-нибудь другие проблемы на стороне серверов Telegram. Попробуйте перезагрузить бота, проверить ваше интернет-соединение, просто ждать</i>.')

    await bot.edit_message_media(chat_id=callback.message.chat.id,
                                 message_id=callback.message.message_id,
                                 media=photo,
                                 reply_markup=create_help_kb())

    return None
