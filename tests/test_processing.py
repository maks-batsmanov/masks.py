
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_01(list_of_dict_for_tests: list) -> None:
    assert filter_by_state(list_of_dict_for_tests) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


def test_filter_by_state_02(list_of_dict_for_tests: list) -> None:
    assert filter_by_state(list_of_dict_for_tests, state='CANCELED') == [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


def test_filter_by_state_03(list_of_dict_for_tests: list) -> None:
    assert filter_by_state(list_of_dict_for_tests, state='') == 'Такого ключа нет'


def test_sort_by_date_01(list_of_dict_for_tests: list) -> None:
    assert sort_by_date(list_of_dict_for_tests) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


def test_sort_by_date_02(list_of_dict_for_tests: list) -> None:
    assert sort_by_date(list_of_dict_for_tests, direction=False) == [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ]


def test_sort_by_date_03(list_of_dict_same_date: list) -> None:
    assert sort_by_date(list_of_dict_same_date) == [
        {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512363'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512362'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512361'}
    ]


def test_sort_by_date_04(list_of_dict_incorrect: list) -> None:
    assert sort_by_date(list_of_dict_incorrect) == 'Неверный формат даты'
