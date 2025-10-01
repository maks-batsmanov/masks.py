
from src.masks import get_mask_card_number
from src.masks import get_mask_account

def test_get_mask_card_number():
    assert get_mask_card_number('1234567812345678') == '1234 56** **** 5678'
    assert get_mask_card_number('121455325322634b')  == 'Ошибка. Проверьте правильность ввода'
    assert get_mask_card_number('123456781234567') == 'Ошибка. Проверьте правильность ввода'
    assert get_mask_card_number('') == 'Ошибка. Проверьте правильность ввода'
    assert get_mask_card_number('kjohuhuhiuhuhiuh') == 'Ошибка. Проверьте правильность ввода'
    assert get_mask_card_number('1234 5678 9109 1345') == 'Ошибка. Проверьте правильность ввода'


def test_get_mask_account():
    assert get_mask_account('73654108430135874305') == '**4305'
    assert get_mask_account('1273654108430135874305') == 'Номер счета должен состоять из 20 цифр. Проверьте правильность ввода'
    assert get_mask_account('1273 6541084 301358 743') == 'Ошибка. Некорректный номер счета'
    assert get_mask_account('12736541084301358') == 'Номер счета должен состоять из 20 цифр. Проверьте правильность ввода'
