import pytest

from src.find_calculate import print_form, find_str

@pytest.mark.parametrize(
    "value, expected",
    [
        ([{
            "id": 490100847,
            "state": "EXECUTED",
            "date": "2018-12-22T02:02:49.564873",
            "operationAmount": {
                "amount": "56516.63",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Gold 8326537236216459",
            "to": "MasterCard 6783917276771847"
        },
        {
            "id": 619287771,
            "state": "EXECUTED",
            "date": "2019-08-19T16:30:41.967497",
            "operationAmount": {
              "amount": "81150.87",
              "currency": {
                "name": "USD",
                "code": "USD"
              }
            },
            "description": "Перевод организации",
            "from": "Счет 17691325653939384901",
            "to": "Счет 49304996510329747621"
          }],
         [{
            "id": 619287771,
            "state": "EXECUTED",
            "date": "2019-08-19T16:30:41.967497",
            "operationAmount": {
              "amount": "81150.87",
              "currency": {
                "name": "USD",
                "code": "USD"
              }
            },
            "description": "Перевод организации",
            "from": "Счет 17691325653939384901",
            "to": "Счет 49304996510329747621"
          }])
    ],
)
def test_find_str(value, expected):
    find_str(value) == expected
