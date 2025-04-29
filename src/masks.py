import logging
from pathlib import Path
from typing import Union

from config import ROOT_DIR

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s: %(message)s ",
    filename=Path.joinpath(ROOT_DIR, "logs", "logs_masks.txt"),
    filemode="w",
    encoding="utf-8",
)
masks_logger = logging.getLogger("masks.py")
masks_handler = logging.FileHandler(Path.joinpath(ROOT_DIR, "logs", "logs_masks.txt"))
masks_handler.encoding = "utf-8"
masks_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s ")
masks_handler.setFormatter(masks_formatter)
masks_logger.addHandler(masks_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Union[int]) -> str:
    """Маскирует платежную карту пользователя в формате XXXX XX** **** XXXX"""
    str_card_number = str(card_number)
    if len(str_card_number) == 16:
        masks_logger.info("Ваша платежная карта зашифрована")
        return str_card_number[:4:] + " " + str_card_number[4:6:] + "** **** " + str_card_number[12::]
    masks_logger.error("Err: некорректный ввод")
    return "Некорректный ввод"


def get_mask_account(account_number: Union[int]) -> str:
    """Маскирует аккаунт пользователя в формате **XXXX"""
    str_account_number = str(account_number)
    if len(str_account_number) == 20:
        masks_logger.info("Ваш аккаунт зашифрован")
        return f"**{str_account_number[-4::]}"
    masks_logger.error("Err: некорректный ввод")
    return "Некорректный ввод"


# print(get_mask_card_number(1234567890123456))
# print(get_mask_account(12345678901234567890))
