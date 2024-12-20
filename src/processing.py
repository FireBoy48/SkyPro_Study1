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
    return f"{dict_time['day']}{dict_time['month']}{dict_time['year']}"


def filter_by_state(base_idtime: list, state: str = "EXECUTED") -> list:
    """
    Сортирует список по параметру state
    """
    output = []
    for unit in base_idtime:
        if unit["state"] == state:
            output.append(unit)
    return output


def sort_by_date(base_idtime: list, reverse: bool = True) -> list:
    """
    Сортирует список по дате
    """
    return sorted(base_idtime, key=lambda x: x["date"], reverse=reverse)


user_input = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


#print(filter_by_state(user_input))
#print(sort_by_date(user_input)) 
