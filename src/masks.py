
def get_mask_card_number(number_of_card: str) -> str:
    """Функция, принимает строку с номером карты и возвращает ее маску"""
    if not str(number_of_card).isdigit():
        return 'Ошибка. Проверьте правильность ввода'
    else:
        digits_list = [int(d) for d in str(number_of_card)]
    if len(digits_list) != 16:
        return 'Ошибка. Проверьте правильность ввода'
    else:
        block_1 = "".join(map(str, digits_list[0:4]))
        block_2 = "".join(map(str, digits_list[4:6]))
        block_3 = "".join(map(str, digits_list[12:]))

        return f"{block_1} {block_2}** **** {block_3}"


def get_mask_account(number_of_account: str) -> str:
    """Функция принимает на вход строку с номером счета и возвращает его маску"""
    if not str(number_of_account).isdigit():
        return 'Ошибка. Некорректный номер счета'
    elif len(number_of_account) != 20:
        return 'Номер счета должен состоять из 20 цифр. Проверьте правильность ввода'
    digits_list = [int(d) for d in str(number_of_account)]
    last_block = "".join(map(str, digits_list[-4:]))
    return f"**{last_block}"
