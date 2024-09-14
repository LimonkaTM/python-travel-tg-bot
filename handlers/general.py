from aiogram import F
from aiogram.dispatcher.router import Router

from aiogram.types import CallbackQuery


router = Router(name="generalRouter")


@router.callback_query(F.data == "close_msg")
async def close_msg(callback: CallbackQuery, ) -> None:

    '''
    Обработка нажатия на кнопку "Назад" для удаления сообщения
    '''

    await callback.message.delete()
