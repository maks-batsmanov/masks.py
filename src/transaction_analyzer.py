import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """ Функция, принимает список словарей
    с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка.
    """

    result_list = []
    pattern = re.compile(search, re.IGNORECASE)
    for dict_ in data:
        # print(dict_)
        match = pattern.search(dict_['description'])
        if match:
            result_list.append(dict_)
        else:
            continue
    if result_list == 0:
        print('Совпадений не найдено')
        return []
    return result_list


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция, принимает список словарей с данными
    о банковских операциях и список категорий операций, а возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории"""

    list_categories = []
    for dict_ in data:
        if dict_['description'] in categories:
            list_categories.append(dict_['description'])
    count = Counter(list_categories)
    return dict(count)
