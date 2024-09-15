from logging import Logger, getLogger, basicConfig, INFO

import asyncio

from loader import bot, dp

from handlers import (
    general, commands, attraction, audio_gid, about, help, feedback, game
)

from keyboards.menu import create_bot_menu


logger: Logger = getLogger(__name__)


async def main() -> None:

    '''
    Функция конфигурирования и запуска бота
    '''

    basicConfig(
        level=INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Starting bot')

    await bot.set_my_commands(create_bot_menu())

    dp.include_routers(
        general.router, commands.router, attraction.router,
        audio_gid.router, about.router, help.router,
        feedback.router, game.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped!')
