from src.reading_tables import read_csv, read_excel
from src.utils import get_transaction_data
from src.processing import filter_by_state
from src.processing import sort_by_date
from src.generators import filter_by_currency
from src.transaction_analyzer import process_bank_search


def main():
    """Функция получает информацию от пользователя и связывает все функциональности"""

    print("""Программа: Привет! Добро пожаловать в программу работы 
        с банковскими транзакциями. Выберите необходимый пункт меню:
        
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла""")

    while True:
        print()
        users_answer = input('Ввод: ')
        print()
        if users_answer == '1':
            print('Для обработки выбран JSON-файл')
            json_path = input('Введите путь к JSON-файлу: ')
            json_path = json_path.strip('"\'')
            res = get_transaction_data(json_path)
            break

        elif users_answer == '2':
            print('Для обработки выбран CSV-файл')
            csv_path = input('Введите путь к CSV-файлу: ')
            csv_path = csv_path.strip('"\'')
            res = read_csv(csv_path)
            break

        elif users_answer == '3':
            print('Для обработки выбран XLSX-файл')
            xlsx_path = input('Введите путь к XLSX-файлу: ')
            xlsx_path = xlsx_path.strip('"\'')
            res = read_excel(xlsx_path)
            break

        else:
            print('Неверно выбран пункт меню. Выберите пункт из предложенных')

    if not res:
        print('Не удалось загрузить данные. Завершение работы.')
        return []

    print()
    print("""Введите статус, по которому необходимо выполнить фильтрацию. 
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
    print()

    while True:
        try:
            users_answer_2 = input('Ввод: ')

            if users_answer_2.upper() == 'EXECUTED':
                filtred_result = filter_by_state(res, 'EXECUTED')
                print('Операции отфильтрованы по статусу EXECUTED')
                break

            elif users_answer_2.upper() == 'CANCELED':
                filtred_result = filter_by_state(res, 'CANCELED')
                print('Операции отфильтрованы по статусу CANCELED')
                break

            elif users_answer_2.upper() == 'PENDING':
                filtred_result = filter_by_state(res, 'PENDING')
                print('Операции отфильтрованы по статусу PENDING')
                break

            else:
                print(f'Статус операции {users_answer_2} недоступен.')

        except Exception as ex:
            print(f'Ошибка {ex}. Попробуйте другой статус')



    print()
    print('Отсортировать операции по дате? Да/Нет')
    print()

    while True:
        users_answer_3 = input()
        if users_answer_3.lower() == 'да':
            print('Отсортировать по возрастанию или по убыванию? (по возрастанию/по убыванию/не сортировать)')
            users_answer_4 = input('Ввод: ')

            if users_answer_4.lower() == 'по возрастанию':
                sorted_result = sort_by_date(filtred_result, False)
                break

            elif users_answer_4.lower() == 'по убыванию':
                sorted_result = sort_by_date(filtred_result, True)
                break

            elif users_answer_4.lower() == 'не сортировать':
                sorted_result = filtred_result
                print('Отмена сортировки')
                break

            else:
                continue

        elif users_answer_3.lower() == 'нет':
            sorted_result = filtred_result
            break

        else:
            print('Выберите один из вариантов')


    print()
    print('Выводить только рублевые транзакции? Да/Нет')
    print()
    while True:
        users_answer_5 = input()
        if users_answer_5.lower() == 'да':
            currency_iterator = filter_by_currency(sorted_result, 'RUB')
            currency_result = list(currency_iterator)
            break
        elif users_answer_5.lower() == 'нет':
            currency_result = sorted_result
            break
        else:
            print('Введите да/нет')


    print()
    print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
    print()
    while True:
        users_answer_6 = input()
        if users_answer_6.lower() == 'да':
            print()
            print('Введите слово для фильтрации:')
            print()
            users_answer_7 = input()
            result_search = process_bank_search(currency_result, users_answer_7)
            break
        elif users_answer_6.lower() == 'нет':
            result_search = currency_result
            break
        else:
            print('Некорректный ввод. Введите да/нет')

    print('Распечатываю итоговый список транзакций...')
    return result_search


print(main())










#
# PENDING"D:\SkyPro_files\transactions_excel.xlsx"
#
# {'id': 632926.0,
#  'state': 'PENDING',
#  'date': '2021-11-27T00:46:09Z',
#  'amount': 29553.0,
#  'currency_name': 'Yuan Renminbi',
#  'currency_code': 'CNY',
#  'from': 'American Express 6477627838877562',
#  'to': 'Счет 88381741644903346269',
#  'description': 'Перевод организации'}













