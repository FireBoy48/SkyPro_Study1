from typing import Union


def get_mask_card_number(card_number: Union[int]) -> str:
    """Маскирует платежную карту пользователя в формате XXXX XX** **** XXXX"""
    str_card_number = str(card_number)
    return str_card_number[:4:] + " " + str_card_number[4:6:] + "** **** " + str_card_number[12::]


def get_mask_account(account_number: Union[int]) -> str:
    """Маскирует аккаунт пользователя в формате **4305"""
    str_account_number = str(account_number)
    return f"**{str_account_number[-4::]}"
