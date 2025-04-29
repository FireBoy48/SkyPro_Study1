from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """Маскирует номер счета или карты пользователя"""
    score_number = card_number.split()
    if len(score_number[-1]) == 16:
        return " ".join(score_number[:-1:]) + " " + get_mask_card_number(int(score_number[-1]))
    if len(score_number[-1]) == 20:
        return f"Счет: {get_mask_account(int(score_number[-1]))}"
    else:
        return "Некорректный ввод"


def get_date(time: str) -> str:
    """Переводит дату в удобный формат"""
    date = list(map(int, time.split("T")[0].split("-")))
    clock = list(map(int, time.split("T")[1].split(":")[:-1:]))
    # second = float(time.split("T")[1].split(":")[-1])
    dict_time = {
        "year": date[0],
        "month": date[1],
        "day": date[2],
        "hour": clock[0],
        "minute": clock[1],
        # "second": second,
    }
    if (
        1 <= dict_time["month"] <= 12
        and 1 <= dict_time["day"] <= 31
        and 1 <= dict_time["hour"] <= 24
        and 1 <= dict_time["minute"] <= 60
        # and 1 <= dict_time["second"] <= 60
    ):
        return f"{"{:02d}".format(dict_time['day'])}.{"{:02d}".format(dict_time['month'])}.{dict_time['year']}"
    return "Некорректный ввод"


# print(get_date('2022-08-24T14:32:38Z;16652'))
