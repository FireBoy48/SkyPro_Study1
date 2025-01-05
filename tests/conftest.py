import pytest


# MASKS
# fixture для get_mask_account
@pytest.fixture
def card():
    return ("1234 56** **** 1121", "1234 56** **** 8765", "Некорректный ввод")


# fixture для get_mask_card_number
@pytest.fixture
def account():
    return ("**4321", "Некорректный ввод")


# WIDGET
# fixture для mask_account_card
@pytest.fixture
def account_card():
    return ("1234 56** **** 1121", "**4321", "Некорректный ввод")


# fixture для get_date
@pytest.fixture
def date():
    return ("28.12.2024", "Некорректный ввод")


# PROCESSING
# fixture для filter_by_state
@pytest.fixture
def state():
    return (
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ],
        [
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
    )


@pytest.fixture
# fixture для sort_by_date
def sort_date():
    return (
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ],
        [
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        ],
    )
