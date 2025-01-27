import json
import logging
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

from config import ROOT_DIR

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s: %(message)s ",
    filename=Path.joinpath(ROOT_DIR, "logs", "logs_utils.txt"),
    filemode="w",
    encoding="utf-8",
)
utils_logger = logging.getLogger("utils.py")


PATH_TO_DATA = Path.joinpath(ROOT_DIR, "data", "operations.json")


def load_data_json(path_to_file: str) -> list:
    """
    Возвращает данные из файла json банковских переводов в формате json-строки
    :param path_to_file: путь до json файла
    :return: данные из файла json банковских переводов в формате json-строки
    """

    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            utils_logger.info(f"Открыт файл {path_to_file}")
            data_operations = json.load(file)
            if not isinstance(data_operations, list):
                data_operations = []
    except FileNotFoundError as fnfe:
        utils_logger.error(f"Ошибка {fnfe}")
        data_operations = []
    except json.JSONDecodeError as decode_err:
        utils_logger.error(f"Ошибка {decode_err}")
        data_operations = []
    except Exception as other:
        utils_logger.error(f"Ошибка {other}")
        data_operations = []

    return data_operations


def parsing_data(data_operations: list, num_transaction: int = 1) -> tuple:
    """
    Возвращает данные о сумме транзакции и валюте в которой она была проведена
    :param data_operations: data_operations это информация о транзакциях в виде json-строки
    :param num_transaction: порядковый номер транзакции
    :return: (сумма, валюта)
    """
    num_transaction -= 1
    if data_operations == []:
        amount = 0
        currency_code = "RUB"
    else:
        amount = float(data_operations[num_transaction]["operationAmount"]["amount"])
        currency_code = data_operations[num_transaction]["operationAmount"]["currency"]["code"]
    return amount, currency_code


def external_api(amount: float, currency_code_from: str, currency_code_to: str = "RUB") -> float:
    """
    Переводит сумму в другую валюту
    :param amount: сумма транзакции
    :param currency_code_from: валюта проведения транзакции
    :param currency_code_to: валюта в которую переводят
    :return:
    """
    if currency_code_from != currency_code_to:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_code_to}&from={currency_code_from}&amount={amount}"

        load_dotenv()
        headers = {"apikey": os.getenv("API_KEY")}
        utils_logger.info(f"Подключение к {url}")
        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            utils_logger.info("Подключение успешно")
            return float(response.json()["result"])
        else:
            utils_logger.info(f"Запрос не был успешным. Возможная причина: \n {response.reason}")
            return response.reason

    else:
        return amount


load_dotenv()
print(external_api(*parsing_data(load_data_json(PATH_TO_DATA), 2)))
