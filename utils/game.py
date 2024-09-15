def is_passed(score: int, question_count: int) -> bool:
    percents = round((100 * score) / question_count, 0)
    print(percents)

    return int(percents) >= 80
