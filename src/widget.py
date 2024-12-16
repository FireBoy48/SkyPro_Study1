def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер счета или карты пользователя"""
    score_number = card_number.split()
    str_score_number = str(score_number[-1])
    if len(str_score_number) == 12:
        return (
            " ".join(score_number[:-1:])
            + " "
            + str_score_number[:4:]
            + " "
            + str_score_number[4:6:]
            + "** **** "
            + str_score_number[12::]
        )
    if len(str_score_number) == 20:
        return f"Счет: **{str_score_number[-4::]}"


def get_date(time: str) -> str:
    """Переводит дату в удобный формат"""
    date = time.split("T")[0].split("-")
    clock = time.split("T")[1].split(":")
    dict_time = {
        "year": date[0],
        "month": date[1],
        "day": date[2],
        "hour": clock[0],
        "minute": clock[1],
        "second": clock[2],
    }
    return f"{dict_time['day']}.{dict_time['month']}.{dict_time['year']}"
