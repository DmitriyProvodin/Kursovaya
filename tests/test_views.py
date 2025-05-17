from src.views import print_transactions, print_summary
from io import StringIO
import sys


def test_print_transactions(capsys):
    data = [
        {
            "date": "2024-01-01T12:00:00",
            "description": "Тест",
            "operationAmount": {"amount": 100, "currency": {"code": "RUB"}}
        }
    ]
    print_transactions(data)
    captured = capsys.readouterr()
    assert "Тест" in captured.out
    assert "100 RUB" in captured.out


def test_print_summary(capsys):
    summary = {"Еда": 3, "Одежда": 2}
    print_summary(summary)
    captured = capsys.readouterr()
    assert "Еда" in captured.out
    assert "3" in captured.out
