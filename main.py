from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.reading_tables import read_csv, read_excel
from src.transaction_analyzer import process_bank_search
from src.utils import get_transaction_data


def main_start():
    """Функция предлагает меню для выбора типа исходного файла"""

    print("""Программа: Привет! Добро пожаловать в программу работы
        с банковскими транзакциями. Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла
        4. Завершить работу""")

    while True:
        print()
        users_answer = input('Ввод: ')
        print()
        if users_answer == '1':
            print('Для обработки выбран JSON-файл')
            json_path = input('Введите путь к JSON-файлу: ')
            json_path = json_path.strip('"\'')
            result = get_transaction_data(json_path)
            if not result:
                print('Не удалось загрузить данные. Завершение работы.')
                return []
            return result

        elif users_answer == '2':
            print('Для обработки выбран CSV-файл')
            csv_path = input('Введите путь к CSV-файлу: ')
            csv_path = csv_path.strip('"\'')
            result = read_csv(csv_path)
            if not result:
                print('Не удалось загрузить данные. Завершение работы.')
                return []
            return result

        elif users_answer == '3':
            print('Для обработки выбран XLSX-файл')
            xlsx_path = input('Введите путь к XLSX-файлу: ')
            xlsx_path = xlsx_path.strip('"\'')
            result = read_excel(xlsx_path)
            if not result:
                print('Не удалось загрузить данные. Завершение работы.')
                return []
            return result

        elif users_answer == '4':
            print('Работа завершена')
            return None

        else:
            print('Неверно выбран пункт меню. Выберите пункт из предложенных')


def main_filtered_status(data_transact):
    """Функция предлагает выбрать тип фильтрации, отправляет данные целевой функции и получает ответ"""
    print()
    print("""Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
    print()

    while True:
        try:
            users_answer = input().strip().upper()
            if users_answer in ['EXECUTED', 'CANCELED', 'PENDING']:
                filtered_result = filter_by_state(data_transact, users_answer)

                if not filtered_result:
                    print(f'Нет транзакций со статусом {users_answer}')
                    print('Попробуйте другой статус')
                    continue
                print(f'Операции отфильтрованы по статусу {users_answer}')
                return filtered_result

            elif users_answer.lower() == 'exit':
                print('Завершение работы')
                return []

            else:
                print(f'Статус {users_answer} не найден')

        except Exception as ex:
            print(f'Ошибка {ex}. Попробуйте другой статус')


def main_sorted_by_date(data_transact):
    """Функция предлагает отсортировать транзакции по дате. Обращается к целевой функции"""
    print()
    print('Отсортировать операции по дате? Да/Нет')
    print()

    while True:
        users_answer = input()
        if users_answer.strip().lower() == 'да':
            while True:
                print('Отсортировать по возрастанию или по убыванию? (по возрастанию/по убыванию/не сортировать)')
                users_answer_2 = input('Ввод: ')

                if users_answer_2.strip().lower() == 'по возрастанию':
                    sorted_result = sort_by_date(data_transact, False)
                    return sorted_result

                elif users_answer_2.strip().lower() == 'по убыванию':
                    sorted_result = sort_by_date(data_transact, True)
                    return sorted_result

                elif users_answer_2.strip().lower() == 'не сортировать':
                    print('Отмена сортировки')
                    return data_transact

                else:
                    print('Выберите один из вариантов')
                    continue

        elif users_answer.strip().lower() == 'нет':
            return data_transact

        else:
            print('Выберите один из вариантов')


def main_filtered_rub_transact(data_transact):
    """Функция предлагает выводить только рублевые транзакции и обращается к целевой функции"""

    try:
        print()
        print('Выводить только рублевые транзакции? Да/Нет')
        print()
        while True:
            users_answer = input()
            if users_answer.strip().lower() == 'да':
                currency_iterator = filter_by_currency(data_transact, 'RUB')
                currency_result = list(currency_iterator)

                if not currency_result:
                    print('Не удалось отфильтровать рублевые транзакции.')
                    return data_transact

                return currency_result

            elif users_answer.strip().lower() == 'нет':
                return data_transact
            else:
                print('Введите да/нет')
    except Exception as ex:
        print(f'Ошибка при фильтрации: {ex}')
        print('Возвращаем исходные данные')
        return data_transact


def main_sorting_by_word(data_transact):
    """Функция предлагает отфильтровать список транзакций по определенному слову в описании """

    print()
    print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
    print()

    while True:
        users_answer = input('Ввод ')
        if users_answer.strip().lower() == 'да':
            print()
            print('Введите слово для фильтрации:')
            print()
            users_answer_2 = input('Ввод ')
            result_search = process_bank_search(data_transact, users_answer_2)

            if not result_search:
                print('По данному слову транзакций не найдено')
                print('Возвращаем исходный файл')
                return data_transact

            return result_search

        elif users_answer.lower() == 'нет':
            return data_transact

        else:
            print('Некорректный ввод. Введите да/нет')


def main_result(data_transact):
    if not data_transact:
        print('Нет транзакций для отображения')
        return None

    print('Распечатываю итоговый список транзакций...')
    print()
    print("=" * 50)

    for i, transaction in enumerate(data_transact, 1):
        print(f"\n--- Транзакция {i} ---")

        for key, value in transaction.items():
            formatted_key = key.replace('_', ' ').title()
            print(f"  {formatted_key}: {value}")
    return data_transact


def main():
    data = main_start()
    if not data:
        return []

    data = main_filtered_status(data)
    data = main_sorted_by_date(data)
    data = main_filtered_rub_transact(data)
    data = main_sorting_by_word(data)
    data = main_result(data)

    return data
