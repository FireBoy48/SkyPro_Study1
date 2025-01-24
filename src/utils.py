import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv
from mypy.types import AnyType

from config import ROOT_DIR

PATH_TO_DATA = Path.joinpath(ROOT_DIR, "data", "operations.json")


def load_data_json(path_to_file: str) -> list:
    """
    Возвращает данные из файла json банковских переводов в формате json-строки
    :param path_to_file: путь до json файла
    :return: данные из файла json банковских переводов в формате json-строки
    """

    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            data_operations = json.load(file)
            if type(data_operations) != dict:
                data_operations = []
    except Exception:
        data_operations = []
    return data_operations
print(load_data_json(PATH_TO_DATA))

def parsing_data(data_operations: list, num_transaction: int = 1) -> tuple:
    """
    Возвращает данные о сумме транзакции и валюте в которой она была проведена
    :param data_operations: data_operations это информация о транзакциях в виде json-строки
    :param num_transaction: порядковый номер транзакции
    :return: (сумма, валюта)
    """
    num_transaction -= 1
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

        response = requests.request("GET", url, headers=headers)

        return float(response.json()["result"])

    else:
        return amount


load_dotenv()
