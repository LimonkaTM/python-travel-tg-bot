from aiogram.types import BotCommand


def create_bot_menu():
    list_command = [
        BotCommand(command='/start',
                   description='Запустить/перезапустить бота'),
        BotCommand(command='/help',
                   description='Справка пользователя')]

    return list_command
