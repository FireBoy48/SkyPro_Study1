import re
from pkgutil import get_data

from src.widget import get_date
from  widget import mask_account_card
from utils import parsing_data


def find_str( some_list: list)-> list:
    some_str = input('Введите искомое слово: ')
    result = []
    for dictionary in some_list:
        if re.findall(some_str, dictionary['description'], flags=0):
                result.append(dictionary)
    return result


def print_form(some_list: list)-> str:
    for item in some_list:
        date = get_date(item['date'])
        category = item["description"]
        froms = mask_account_card(item['from'])
        to = mask_account_card(item['to'])
        amount, currency_code = parsing_data(item)
    return f'''
    {date} {category}
    {froms} -> {to}
    Сумма: {amount} {currency_code}
    '''

