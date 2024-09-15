def calc_percent_true_answers(score: int, question_count: int) -> int:
    '''
    Расчитывает процент верных ответов

    Args:
        score (int): кол-во правильных ответов
        question_count (int): общее кол-во вопросов

    Returns:
        Процент верных ответов
    '''

    percents = round((100 * score) / question_count, 0)

    return int(percents)


def define_type_game_result(score_persent: str) -> str:
    '''
    Определяет тип игрового реузльтата

    Args:
        score_persent (int): процент правильных ответов

    Returns:
        'pro' or 'middle' or 'junior' (str)
    '''

    if score_persent >= 80:
        return 'pro'
    elif score_persent > 50 & score_persent < 80:
        return 'middle'
    else:
        return 'junior'
