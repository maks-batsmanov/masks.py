from unittest.mock import patch

from src.external_api import get_amount_transactions


@patch("requests.request")
def test_get_amount_transactions_01(mock_requests):
    mock_requests.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 978.31},
        "info": {"timestamp": 1761422294, "rate": 79.61906},
        "date": "2025-10-25",
        "result": 77892.122589,
    }
    assert (
        get_amount_transactions(
            {
                "id": 743628025,
                "state": "EXECUTED",
                "date": "2018-06-04T06:59:55.424356",
                "operationAmount": {"amount": "978.31", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 54883981902864782073",
                "to": "Счет 61834060137088759145",
            }
        )
        == 77892.122589
    )


def test_get_amount_transactions_02():
    assert (
        get_amount_transactions(
            {
                "id": 587085106,
                "state": "EXECUTED",
                "date": "2018-03-23T10:45:06.972075",
                "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Открытие вклада",
                "to": "Счет 41421565395219882431",
            }
        )
        == 48223.05
    )
