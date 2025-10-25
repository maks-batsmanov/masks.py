import os
from dotenv import load_dotenv
import requests


def get_amount_transactions(trans: dict): #-> float:
    """ Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API
    и конвертации суммы операции в рубли."""


    if trans["operationAmount"]["currency"]["code"] == "RUB":
        return trans["operationAmount"]["amount"]

    else:
        from_currency = trans["operationAmount"]["currency"]["code"]
        amount = trans["operationAmount"]["amount"]

        load_dotenv('.env')
        api_key = os.getenv('API_KEY')
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_currency}&amount={amount}"
        payload = {}
        headers = {
            "apikey": api_key
        }

        response = requests.request("GET", url, headers=headers, data = payload)
        return response.text



transactions = {
    "id": 743628025,
    "state": "EXECUTED",
    "date": "2018-06-04T06:59:55.424356",
    "operationAmount": {
      "amount": "978.31",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 54883981902864782073",
    "to": "Счет 61834060137088759145"
  }
if __name__ == '__main__':
    print(get_amount_transactions(transactions))