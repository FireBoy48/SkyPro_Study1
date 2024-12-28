import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Master Card 1234567891011121", "1234 56** **** 1121"),
        ("Счет 12345678900987654321", "**4321"),
        ("банка №1", "Некорректный ввод"),
    ],
)
def test_mask_account_card(value, expected):
    mask_account_card(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [("2024-12-28T02:26:18.671407", "28.12.2024"), ("2077-28-13T02:26:18.671407", "Некорректный ввод")],
)
def test_get_date(value, expected):
    get_date(value) == expected
    with pytest.raises(ValueError):
        get_date("alpha_value")
