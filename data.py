import json


def get_JSON(fileName: str) -> dict:
    '''
    Читает JSON из файла

    Читает данные из JSON файла и возвращает JSON
    Args:
        fileName (str): имя JSON файла из которго читаем JSON
    Returns:
        dict: JSON данные в формате dict
    '''

    with open(fileName, 'r', encoding='utf-8') as file:
        return json.load(file)
