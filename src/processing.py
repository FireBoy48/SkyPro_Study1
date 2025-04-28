from config import ROOT_DIR
from pathlib import Path
transactions_json = Path.joinpath(ROOT_DIR, "data", "operations.json")

def filter_by_state(base_idtime: list, state: str = "EXECUTED") -> list:
    """
    Сортирует список по параметру state
    """
    output = []
    for unit in base_idtime:
        if 'state' in unit:
            if unit["state"] == state:
                output.append(unit)
    return output


def sort_by_date(base_idtime: list, reverse: bool = True) -> list:
    """
    Сортирует список по дате
    """
    return sorted(base_idtime, key=lambda x: x["date"], reverse=reverse)





# print(filter_by_state(user_input))
# print(sort_by_date(user_input))
