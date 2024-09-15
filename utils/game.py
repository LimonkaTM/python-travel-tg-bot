def calc_percent_true_answers(score: int, question_count: int) -> int:
    percents = round((100 * score) / question_count, 0)

    return int(percents)


def define_type_game_result(score: str) -> str:
    if score >= 80:
        return 'pro'
    elif score > 50 & score < 80:
        return 'middle'
    else:
        return 'junior'
