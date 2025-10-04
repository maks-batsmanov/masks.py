import pytest

@pytest.fixture
def list_of_dict_for_tests():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

@pytest.fixture
def list_of_dict_same_date():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512361'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512362'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512363'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}
        ]


@pytest.fixture
def list_of_dict_incorrect():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-02-07'},
        ]

@pytest.fixture
def number_of_card_01():
    return 'Visa Platinum 7000792289606361'

@pytest.fixture
def number_of_card_02():
    return 'Maestro 7000792289606361'

@pytest.fixture
def number_of_account():
    return 'Счет 73654108430135874305'

