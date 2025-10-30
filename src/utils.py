import json
import logging
import os

current_file_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_file_dir)  # Поднимаемся на уровень выше
log_dir = os.path.join(project_root, "logs")
log_file = os.path.join(log_dir, "masks.log")
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(filename)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transaction_data(path_to_file: str) -> list:
    """Функция принимает путь к json-файлу, и возвращает список словарей с данными о транзакциях
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список"""

    logger.info(f"Начало работы функции. Входные данные: {path_to_file}")
    normalized_path = os.path.normpath(path_to_file)

    if not os.path.exists(normalized_path):
        logger.error("Ошибка, файл не найден")
        return []
    if os.path.getsize(normalized_path) == 0:
        logger.error("Ошибка, файл пустой")
        return []
    logger.info("Открываем и преобразуем файл в список словарей")
    with open(normalized_path, "r", encoding="utf-8") as file:
        content = json.load(file)
    if not isinstance(content, list):
        logger.error("Ошибка, файл не является списком")
        return []
    logger.info("Работа завершена успешно")
    return content
