import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize('value, expected', [
    ('1234567812345678', '1234 56** **** 5678'),
    ('121455325322634b', 'Ошибка. Проверьте правильность ввода'),
    ('123456781234567', 'Ошибка. Проверьте правильность ввода'),
    ('', 'Ошибка. Проверьте правильность ввода'),
    ('kjohuhuhiuhuhiuh', 'Ошибка. Проверьте правильность ввода'),
    ('1234 5678 9109 1345', 'Ошибка. Проверьте правильность ввода')
])
def test_get_mask_card_number(value: str, expected: str) -> None:
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize('value, expected', [
    ('73654108430135874305', '**4305'),
    ('1273654108430135874305', 'Номер счета должен состоять из 20 цифр. Проверьте правильность ввода'),
    ('1273 6541084 301358 743', 'Ошибка. Некорректный номер счета'),
    ('12736541084301358', 'Номер счета должен состоять из 20 цифр. Проверьте правильность ввода')
])
def test_get_mask_account(value: str, expected: str) -> None:
    assert get_mask_account(value) == expected
