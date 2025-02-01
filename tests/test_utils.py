import json
import os
from pathlib import Path
from unittest.mock import patch

from dotenv import load_dotenv

from config import ROOT_DIR
from src.utils import external_api, load_data_json, parsing_data


def test_load_data_json():
    path_to_file = Path.joinpath(ROOT_DIR, "data", "test.json")

    with open(path_to_file, "w") as f:
        json.dump([{"object": [1, 2]}], f)

    expected_data = [{"object": [1, 2]}]
    assert load_data_json(path_to_file) == expected_data

    os.remove(path_to_file)


def test_load_data_json_notdict():
    path_to_file = Path.joinpath(ROOT_DIR, "data", "test.json")
    with open(path_to_file, "w") as f:
        json.dump({"object": [1, 2]}, f)
    expected_data = []
    assert load_data_json(path_to_file) == expected_data
    os.remove(path_to_file)


def test_load_data_json_DecodeErr():
    path_to_file = Path.joinpath(ROOT_DIR, "data", "test.json")
    with open(path_to_file, "w") as f:
        json.dump([{True: (1, 2)}], f)
    os.remove(path_to_file)


def test_load_data_json_exeptions():
    assert load_data_json("wrong_path_to_file") == []


def test_parsing_data():
    test_data = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]
    expected_data = (31957.58, "RUB")
    assert parsing_data(test_data, 1) == expected_data


@patch("requests.request")
def test_external_api(mock_requests):
    mock_requests.return_value.json = {"result": 1000}
    assert external_api(1000, "RUB", "RUB") == 1000
    # load_dotenv()
    # url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=10"
    # headers = {"apikey": os.getenv("API_KEY")}
    # mock_requests.assert_called_once_with("GET", url, headers=headers)
