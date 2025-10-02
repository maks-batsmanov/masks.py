
import re

def filter_by_state(list_of_dict: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция принимает список словарей и возвращает новый список,
    содержащий только те словари, у которых ключ state
    соответствует указанному значению."""

    new_list_of_dict = []

    valid_states = ['EXECUTED', 'CANCELED']
    if state not in valid_states:
        return 'Такого ключа нет'
    for dictionary in list_of_dict:
        if dictionary['state'] == state:
            new_list_of_dict.append(dictionary)
    return new_list_of_dict



def sort_by_date(list_of_dict: list[dict], direction: bool = True) -> list[dict]:
    """Функция, которая принимает список словарей,
    и возвращает новый список, отсортированный по дате"""
    pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])T([01]\d|2[0-3]):([0-5]\d):([0-5]\d)\.\d+$"
    for dict_ in list_of_dict:
        if bool(re.match(pattern, dict_['date'])) is False:
            return 'Неверный формат даты'
    list_sorted_by_date = sorted(list_of_dict, key=lambda x: x['date'] , reverse=direction)
    return list_sorted_by_date
