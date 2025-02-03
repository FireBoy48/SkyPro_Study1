import csv
from pathlib import Path

import pandas

from config import ROOT_DIR

transactions_csv = Path.joinpath(ROOT_DIR, "data", "transactions.csv")
transactions_xlsx = Path.joinpath(ROOT_DIR, "data", "transactions_excel.xlsx")


def read_csv(path_to_file: str) -> list:
    """
    Функция для чтения csv файлов
    :param path_to_file: путь до файла CSV
    :return: Список словарей
    """
    with open(path_to_file, "r") as file:
        rows = csv.DictReader(file, delimiter=";")
        list_of_dict = []
        print(rows)
        for row in rows:
            list_of_dict.append(dict(row))
    return list_of_dict


def read_xlsx(path_to_file: str) -> list:
    """
    Функция для чтения xlsx файлов
    :param path_to_file: путь до файла xlsx
    :return: Список словарей
    """
    xlsx = pandas.read_excel(path_to_file)
    print(type(xlsx))
    return xlsx.to_dict("records")


read_xlsx(transactions_xlsx)
