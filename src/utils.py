import json
import os


def get_transaction_data(path_to_file: str) -> list:
    """Функция принимает путь к json-файлу, и возвращает список словарей с данными о транзакциях
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список"""

    normalized_path = os.path.normpath(path_to_file)

    if not os.path.exists(normalized_path):
        return []
    if os.path.getsize(normalized_path) == 0:
        return []
    with open(normalized_path, "r", encoding="utf-8") as file:
        content = json.load(file)
    if not isinstance(content, list):
        return []

    return content
