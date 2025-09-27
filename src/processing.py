
def filter_by_state(list_of_dict: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция принимает список словарей и возвращает новый список,
    содержащий только те словари, у которых ключ state
    соответствует указанному значению."""

    new_list_of_dict = []

    for dictionary in list_of_dict:
        if dictionary['state'] == state:
            new_list_of_dict.append(dictionary)
    return new_list_of_dict


def sort_by_date(list_of_dict: list[dict], direction: bool = True) -> list[dict]:
    """Функция, которая принимает список словарей,
    и возвращает новый список, отсортированный по дате"""
    list_sorted_by_date = sorted(list_of_dict, key=lambda x: x['date'], reverse=direction)
    return list_sorted_by_date
