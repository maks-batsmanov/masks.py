import re

from src import masks


def mask_account_card(card_or_account: str) -> str:
    """Функция обрабатывает информацию о картах и счетах"""
    if "счет" in card_or_account.lower():
        parts = card_or_account.split()
        number = parts[1]
        return f"{parts[0]} {masks.get_mask_account(number)}"
    else:
        parts = card_or_account.split()
        if len(parts) == 2:
            number = parts[1]
            return f"{parts[0]} {masks.get_mask_card_number(number)}"
        else:
            number = parts[2]
            return f"{parts[0]} {parts[1]} {masks.get_mask_card_number(number)}"


def get_date(date: str) -> str:
    """Функция принимает на вход дату и возвращает ее в формате 'ДД.ММ.ГГГГ'"""
    dates = re.findall(r"\d{4}-\d{2}-\d{2}", date)
    return f"{dates[0][8:]}.{dates[0][5:7]}.{dates[0][0:4]}"
