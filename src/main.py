from pkgutil import get_data

from src.find_calculate import find_str, print_form
from src.processing import sort_by_date, filter_by_state
from src.widget import get_date
from utils import load_data_json, parsing_data
from  read_table import read_xlsx, read_csv
from config import ROOT_DIR
from pathlib import Path


transactions_json = Path.joinpath(ROOT_DIR, "data", "operations.json")
transactions_csv = Path.joinpath(ROOT_DIR, "data", "transactions.csv")
transactions_xlsx = Path.joinpath(ROOT_DIR, "data", "transactions_excel.xlsx")


def wrong(status, all_status: list):
    print(f'''Программа: Статус операции {status} недоступен.
    Программа: Введите статус, по которому необходимо выполнить пункт меню. 
    Доступные для фильтровки статусы: {', '.join(all_status)}''')


print('''
Программа: Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
''')
intro = input('Пользователь: ')
while intro not in ['1','2', '3']:
    wrong(intro, ['1','2', '3'])
    intro = input('Пользователь: ')


print('''
Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
''')
state_filter = input('Пользователь: ').upper()
while state_filter not in ['EXECUTED', 'CANCELED', 'PENDING']:
    wrong(state_filter, ['EXECUTED', 'CANCELED', 'PENDING'])
    state_filter = input('Пользователь: ').upper()


print('''
Программа: Отсортировать операции по дате? Да/Нет 
''')
date_filter = input('Пользователь: ').upper()
while date_filter not in ['ДА', 'НЕТ']:
    wrong(date_filter, ['ДА', 'НЕТ'])
    date_filter = input('Пользователь: ').upper()


if date_filter == 'ДА':
    print('''
Программа: Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию
''')
    date_reverse = input('Пользователь: ').upper()
    while date_reverse not in ['ПО ВОЗРАСТАНИЮ', 'ПО УБЫВАНИЮ']:
        wrong(date_reverse, ['ПО ВОЗРАСТАНИЮ', 'ПО УБЫВАНИЮ'])
        date_reverse = input('Пользователь: ').upper()
    if date_reverse == 'ПО ВОЗРАСТАНИЮ':
        date_reverse = False
    else:
        date_reverse = True


print('''
Программа: Выводить только рублевые транзакции? Да/Нет
''')
rubel = (input('Пользователь: ')).upper()
while rubel not in ['ДА', 'НЕТ']:
    wrong(rubel, ['ДА', 'НЕТ'])
    rubel = input('Пользователь: ').upper()


print('''
Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет
''')
discription_filter = (input('Пользователь: ')).upper()
while discription_filter not in ['ДА', 'НЕТ']:
    wrong(discription_filter, ['ДА', 'НЕТ'])
    discription_filter = input('Пользователь: ').upper()


# Тип данных
if intro == '1':
    data = load_data_json(transactions_json)
elif intro == '2':
    data = read_csv(transactions_csv)
elif intro == '3':
    data = read_xlsx(transactions_xlsx)

# Статус
result = filter_by_state(data, state_filter)

# Дата+реверс
if date_filter == 'ДА':
    result = sort_by_date(result, date_reverse)

# Рубли
if rubel == 'ДА':
    subresult = []
    if intro == '1':

        for item in result:
            currency_code = item["operationAmount"]["currency"]["code"]
            if currency_code == 'RUB':
                subresult.append(item)


    if intro in ['3', '2']:
        for item in result:
            if item['currency_code'] == 'RUB':
                subresult.append(item)
    result = subresult

# Описание
if discription_filter == 'ДА':
    result = find_str(result)

print('Программа: Распечатываю итоговый список транзакций...')
print(f'Программа: Всего банковских операций в выборке: {len(result)}')
if intro == '1':
    print(print_form(result))
if intro in ['3', '2']:
    for item in result:
        print(
        f'''
            {get_date(item['date'])} {item["description"]}
            {item['from']} -> {item['to']}
            Сумма: {item['amount']} {item['currency_code']}
            '''
        )

