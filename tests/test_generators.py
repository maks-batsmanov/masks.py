import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_01(transactions_fixture):
    usd_transactions = filter_by_currency(transactions_fixture, key="RUB")
    expected = {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(usd_transactions) == expected


def test_filter_by_currency_02(transactions_fixture):
    usd_transactions = filter_by_currency(transactions_fixture, key="USD")
    expected = {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(usd_transactions) == expected


def test_filter_by_currency_03():
    usd_transactions = filter_by_currency([], key="RUB")
    with pytest.raises(StopIteration):
        next(usd_transactions)


def test_transaction_descriptions_01(transactions_fixture):
    gen = transaction_descriptions(transactions_fixture)
    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод с карты на карту"
    assert next(gen) == "Перевод организации"


def test_transaction_descriptions_02():
    gen = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(gen)


def test_transaction_descriptions_03():
    gen = transaction_descriptions(["1234"])
    with pytest.raises(TypeError):
        next(gen)


def test_card_number_generator_01():
    gen = card_number_generator(1, 5)
    assert next(gen) == "0000 0000 0000 0001"
    assert next(gen) == "0000 0000 0000 0002"
    assert next(gen) == "0000 0000 0000 0003"
    assert next(gen) == "0000 0000 0000 0004"
    assert next(gen) == "0000 0000 0000 0005"


def test_card_number_generator_02():
    gen = card_number_generator(9999999999999991, 9999999999999995)
    assert next(gen) == "9999 9999 9999 9991"
    assert next(gen) == "9999 9999 9999 9992"
    assert next(gen) == "9999 9999 9999 9993"
    assert next(gen) == "9999 9999 9999 9994"
    assert next(gen) == "9999 9999 9999 9995"


def test_card_number_generator_03():
    gen = card_number_generator(123, "125")
    with pytest.raises(TypeError):
        next(gen)
