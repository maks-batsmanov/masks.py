import re

from src import masks


def mask_account_card(card_or_account: str) -> str:
    """Функция обрабатывает информацию о картах и счетах"""
    if card_or_account.find(" ") == -1:
        return "Неверный формат ввода"

    elif "счет" in card_or_account.lower():
        parts = card_or_account.split()
        number = parts[1]
        error_long_nuber = "Номер счета должен состоять из 20 цифр. Проверьте правильность ввода"
        if not number.isdigit():
            return "Неверный формат ввода"
        elif (masks.get_mask_account(number)) == "Ошибка. Некорректный номер счета":
            return "Неверный формат ввода"
        elif (masks.get_mask_account(number)) == error_long_nuber:
            return "Неверный формат ввода"
        return f"{parts[0]} {masks.get_mask_account(number)}"
    else:
        parts = card_or_account.split()
        if len(parts) == 2:
            number = parts[1]
            if masks.get_mask_card_number(number) == "Ошибка. Проверьте правильность ввода":
                return "Неверный формат ввода"
            elif not number.isdigit():
                return "Неверный формат ввода"
            return f"{parts[0]} {masks.get_mask_card_number(number)}"
        else:
            number = parts[2]
            if not number.isdigit():
                return "Неверный формат ввода"
            elif masks.get_mask_card_number(number) == "Ошибка. Проверьте правильность ввода":
                return "Неверный формат ввода"
            return f"{parts[0]} {parts[1]} {masks.get_mask_card_number(number)}"


def get_date(date: str) -> str:
    """Функция принимает на вход дату и возвращает ее в формате 'ДД.ММ.ГГГГ'"""
    pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])T([01]\d|2[0-3]):([0-5]\d):([0-5]\d)\.\d+$"
    if bool(re.match(pattern, date)) is False:
        return "Неверный формат даты"
    dates = re.findall(r"\d{4}-\d{2}-\d{2}", date)
    return f"{dates[0][8:]}.{dates[0][5:7]}.{dates[0][0:4]}"
