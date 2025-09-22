
def filter_by_state(list_of_dict: list[dict], state='EXECUTED') -> list[dict]:
    """Функция принимает список словарей и возвращает новый список,
    содержащий только те словари, у которых ключ state
    соответствует указанному значению."""

    new_list_of_dict = []

    for dictionary in list_of_dict:
        if dictionary['state'] == state:
            new_list_of_dict.append(dictionary)
    return new_list_of_dict

example = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

def sort_by_date(list_of_dict: list[dict], direction=True) -> list[dict]:
    list_sorted_by_date = sorted(list_of_dict, key=lambda x: x['date'], reverse=direction)
    return list_sorted_by_date

print(sort_by_date(example))