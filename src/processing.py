
def filter_by_state(list_of_dict: list[dict], state: str = 'EXECUTED') -> list:
    """Функция принимает список словарей и возвращает новый список,
    содержащий только те словари, у которых ключ state
    соответствует указанному значению."""

    new_list_of_dict = []

    valid_states = ['EXECUTED', 'CANCELED', 'PENDING']
    if state not in valid_states:
        print('Такого ключа нет')
        return []
    for dictionary in list_of_dict:
        if dictionary['state'] == state:
            new_list_of_dict.append(dictionary)
    return new_list_of_dict


def sort_by_date(list_of_dict: list[dict], direction: bool = True) -> list:
    """Функция, которая принимает список словарей,
    и возвращает новый список, отсортированный по дате
    По умолчанию сортирует по убыванию"""

    if not list_of_dict:
        return []

    valid_transactions = [t for t in list_of_dict if t.get('date')]

    try:
        return sorted(valid_transactions, key=lambda x: x['date'], reverse=direction)
    except Exception:
        return list_of_dict
