import logging
import os

current_file_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_file_dir)  # Поднимаемся на уровень выше
log_dir = os.path.join(project_root, 'logs')
log_file = os.path.join(log_dir, 'masks.log')
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(filename)s %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_of_card: str) -> str:
    """Функция, принимает строку с номером карты и возвращает ее маску"""
    logger.info(f'Начало работы с входными данными: {number_of_card}')
    if not str(number_of_card).isdigit():
        logger.warning('Не верно введен номер карты')
        return 'Ошибка. Проверьте правильность ввода'
    else:
        digits_list = [int(d) for d in str(number_of_card)]
    if len(digits_list) != 16:
        logger.warning('Не верно введен номер карты')
        return 'Ошибка. Проверьте правильность ввода'
    else:
        block_1 = "".join(map(str, digits_list[0:4]))
        block_2 = "".join(map(str, digits_list[4:6]))
        block_3 = "".join(map(str, digits_list[12:]))

        logger.info('Работа завершена успешно')
        return f"{block_1} {block_2}** **** {block_3}"


def get_mask_account(number_of_account: str) -> str:
    """Функция принимает на вход строку с номером счета и возвращает его маску"""
    logger.info(f'Начало работы с входными данными: {number_of_account}')
    if not str(number_of_account).isdigit():
        logger.warning('Не верно введен номер счета')
        return 'Ошибка. Некорректный номер счета'
    elif len(number_of_account) != 20:
        logger.warning('Не верно введен номер счета')
        return 'Номер счета должен состоять из 20 цифр. Проверьте правильность ввода'
    digits_list = [int(d) for d in str(number_of_account)]
    last_block = "".join(map(str, digits_list[-4:]))
    logger.info('Работа завершена успешно')
    return f"**{last_block}"
