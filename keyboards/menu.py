from aiogram.types import BotCommand


def create_bot_menu() -> list[BotCommand]:
    '''
    Создаёт разметку комманд бота

    Returns:
        list_command (list[BotCommand]): массив состоящий из объектов
        BotCommand (комманд бота)
    '''

    list_command = [
        BotCommand(
            command='/start',
            description='Запустить бота'
        )
    ]

    return list_command
