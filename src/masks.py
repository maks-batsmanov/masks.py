def get_mask_card_number(number_of_card: [int | str]) -> str:
    """Функция, принимает номер карты и возвращает ее маску"""
    digits_list = [int(d) for d in str(number_of_card)]

    block_1 = "".join(map(str, digits_list[0:4]))
    block_2 = "".join(map(str, digits_list[4:6]))
    block_3 = "".join(map(str, digits_list[12:]))
    return f"{block_1} {block_2}** **** {block_3}"


def get_mask_account(number_of_account: [int | str]) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    digits_list = [int(d) for d in str(number_of_account)]
    last_block = "".join(map(str, digits_list[-4:]))
    return f"**{last_block}"
