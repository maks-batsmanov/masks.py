from unittest.mock import mock_open, MagicMock, patch

from src.reading_tables import read_csv, read_excel


def test_read_csv():

    mock_transactions = [
        {'state': 'EXECTUD', 'amount': 100, 'currency': 'RUB'},
        {'state': 'EXECTUD', 'amount': 200, 'currency': 'EUR'},
        {'state': 'CANCELED', 'amount': 300, 'currency': 'USD'}
    ]

    with patch('builtins.open', mock_open()) as mock_file:
        with patch('csv.DictReader') as mock_reader:
            mock_reader.return_value = mock_transactions

            result = read_csv('test_csv')
            assert result == mock_transactions


def test_read_excel():
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [
        {'id': 1, 'amount': 100, 'currency': 'USD'},
        {'id': 2, 'amount': 200, 'currency': 'EUR'},
        {'id': 3, 'amount': 300, 'currency': 'RUB'}
    ]
    with patch('pandas.read_excel') as mock_read_excel:
        mock_read_excel.return_value = mock_df

        result = read_excel('file.xlsx')

        mock_read_excel.assert_called_once_with('file.xlsx')
        assert result == mock_df.to_dict.return_value
