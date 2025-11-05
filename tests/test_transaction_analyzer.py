from src.transaction_analyzer import process_bank_operations, process_bank_search


def test_process_bank_search(transactions_fixture):
    assert process_bank_search(transactions_fixture, "Перевод со счета на счет") == [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 937764268,
            "state": "EXECUTED",
            "date": "2017-09-04T23:15:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]
    assert process_bank_search(transactions_fixture, "Перевод организации") == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    assert process_bank_search(transactions_fixture, "abc") == []
    assert process_bank_search(transactions_fixture, "Простой перевод") == []


test_list = ["Перевод организации", "Перевод с карты на карту", "Перевод со счета на счет"]


def test_process_bank_operations(transactions_fixture):
    assert process_bank_operations(transactions_fixture, test_list) == {
        "Перевод организации": 2,
        "Перевод с карты на карту": 2,
        "Перевод со счета на счет": 3,
    }
    assert process_bank_operations(transactions_fixture, []) == {}
