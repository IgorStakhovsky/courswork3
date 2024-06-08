from datetime import datetime
import json

def load_operations():
    """Код для загрузки библиотеки operations"""
    with open('../operations.json', 'r', encoding='utf-8') as file:
        operations = json.load(file)
        return operations

def last_five_executed(operations):
    """Сортировка по executed"""
    filtred_list = []
    for operation in operations:
        if operation.get('state') == "EXECUTED":
            filtred_list.append(operation)
    return filtred_list

def last_five_operations(sort_operations):
    """Сортировка по датам, вывод 5ти последних, которые executed"""
    sort_date = sorted(sort_operations, key=lambda x: x.get('date', ''), reverse=True)
    last_five_operations = sort_date[:6]
    return last_five_operations

def sorted_date(list_operations):
    """ Функция меняющая формат дат """
    for operation in list_operations:
        operation['date'] = datetime.fromisoformat(operation['date']).strftime('%d.%m.%Y')
    return list_operations

def format_info_user(value):
    """Эта функция скрывает номера карт и счетов"""
    check = value.split()[-1]
    if len(check) == 16:
        new_check = f'{value[:-len(check)]}{check[:4]} {check[4:6]}** **** {check[-4:]}'
        return new_check

    else:
        new_check2 = f'{value[:-len(check)]}**{check[-4:]}'
        return new_check2