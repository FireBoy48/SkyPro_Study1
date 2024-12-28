import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "value, expected",
    [(1234567891011121, "1234 56** **** 1121"), (1234567890098765, "1234 56** **** 8765"), (1, "Некорректный ввод")],
)
def test_get_mask_card(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize(
    "value, expected", [(12345678910111214321, "**4321"), (1234567890098765, "Некорректный ввод")]
)
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected
