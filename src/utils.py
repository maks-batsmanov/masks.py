import json
import os


def get_transaction_data(path_to_file: str) -> list:
    """Функция принимает путь к файлу, и возвращает список словарей с данными о транзакциях
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список"""

    normalized_path = os.path.normpath(path_to_file)

    if os.path.getsize(normalized_path) == 0:
        return []
    if not os.path.exists(normalized_path):
        return []

    with open(normalized_path, "r", encoding="utf-8") as file:
        content = json.load(file)
    if not isinstance(normalized_path, list):
        return []

    return content
