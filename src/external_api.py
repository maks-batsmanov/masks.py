import os

import requests
from dotenv import load_dotenv


def get_amount_transactions(trans: dict) -> float:
    """ Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API
    и конвертации суммы операции в рубли."""

    if trans["operationAmount"]["currency"]["code"] == "RUB":
        return float(trans["operationAmount"]["amount"])
    else:
        from_currency = trans["operationAmount"]["currency"]["code"]
        amount = trans["operationAmount"]["amount"]

        load_dotenv('.env')
        api_key = os.getenv('API_KEY')
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_currency}&amount={amount}"
        headers = {
            "apikey": api_key
        }
        response = requests.request("GET", url, headers=headers)
        data = response.json()
        return float(data["result"])
