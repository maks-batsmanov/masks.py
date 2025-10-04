import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card_01(number_of_card_01: str) -> None:
    assert mask_account_card(number_of_card_01) == 'Visa Platinum 7000 79** **** 6361'


def test_mask_account_card_02(number_of_card_02: str) -> None:
    assert mask_account_card(number_of_card_02) == 'Maestro 7000 79** **** 6361'


def test_mask_account_card_03(number_of_account: str) -> None:
    assert mask_account_card(number_of_account) == 'Счет **4305'


def test_mask_account_card_04() -> None:
    assert mask_account_card('Счет asdf1658498765489752') == "Неверный формат ввода"


@pytest.mark.parametrize('value, expected', [
    ('Счет1658498765489752', 'Неверный формат ввода'),
    ('Visa Platinum7000792289606361', 'Неверный формат ввода'),
    ('сче 70007922896063617890', 'Неверный формат ввода'),
    ('7000792289606361 Visa Platinum', 'Неверный формат ввода'),
    ('Счет 7000792289606361', 'Неверный формат ввода'),
    ('', 'Неверный формат ввода'),
    ('hyyuuhu huhytdds sfwsf', 'Неверный формат ввода'),
    ('Master card 70007922896063', 'Неверный формат ввода'),
    ('[]', 'Неверный формат ввода'),
])
def test_mask_account_card(value: str, expected: str) -> None:
    assert mask_account_card(value) == expected


@pytest.mark.parametrize('value, expected', [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('', 'Неверный формат даты'),
    (' ', 'Неверный формат даты'),
    ('202-0-11T02:26:18.671407', 'Неверный формат даты'),
    ('hjkf-ij-uyTiu:ws:1wg.671407', 'Неверный формат даты'),
    ('[True, 123.8, ()]', 'Неверный формат даты'),
])
def test_get_date(value: str, expected: str) -> None:
    assert get_date(value) == expected
