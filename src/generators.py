def filter_by_currency(list_of_dict, key):
    """Функция принимает на вход список словарей и ключ. Функция возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует коду,
     указанному в ключе (например, USD)."""
    return (x for x in list_of_dict if x["operationAmount"]["currency"]["code"] == key)


def transaction_descriptions(list_of_dict):
    """Генераторная функция принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""
    for dict_ in list_of_dict:
        yield dict_["description"]


def card_number_generator(first, last):
    """Генераторная функция выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    Может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Принимает начальное и конечное значения для генерации диапазона номеров."""
    for ind in range(first, last + 1):
        str_ind = str(ind)
        x = str_ind.zfill(16)
        yield " ".join([x[i : i + 4] for i in range(0, 16, 4)])
