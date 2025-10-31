import csv

import pandas as pd


def read_csv(path_to_csv):
    """Функция принимает на вход путь до csv-файла и возвращает список словарей с транзакциями"""
    try:
        list_of_dict = []
        with open(path_to_csv) as file:
            reader = csv.DictReader(file, delimiter=';')

            for row in reader:
                list_of_dict.append(row)

            return list_of_dict

    except Exception as ex:
        return f'Ошибка: {ex}'


def read_excel(path_to_excel):
    """Функция принимает на вход путь до excel-файла и возвращает список словарей с транзакциями"""
    try:
        df = pd.read_excel(path_to_excel)
        list_of_dict = df.to_dict('records')

        return list_of_dict

    except Exception as ex:
        return f'Ошибка: {ex}'
