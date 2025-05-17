from src.services import (
    filter_by_status,
    filter_by_currency,
    filter_by_keyword,
    count_by_category,
    filter_by_date_range,
)


sample_data = [
    {
        "status": "EXECUTED",
        "description": "Ozon",
        "date": "2024-01-10T15:00:00",
        "operationAmount": {"amount": 300, "currency": {"code": "RUB"}}
    },
    {
        "status": "CANCELED",
        "description": "M.Video",
        "date": "2024-01-20T18:00:00",
        "operationAmount": {"amount": 500, "currency": {"code": "USD"}}
    }
]


def test_filter_by_status():
    result = filter_by_status(sample_data, "EXECUTED")
    assert len(result) == 1
    assert result[0]["description"] == "Ozon"


def test_filter_by_currency():
    result = filter_by_currency(sample_data, "USD")
    assert len(result) == 1
    assert result[0]["description"] == "M.Video"


def test_filter_by_keyword():
    result = filter_by_keyword(sample_data, "ozon")
    assert len(result) == 1
    assert result[0]["description"] == "Ozon"


def test_filter_by_date_range():
    result = filter_by_date_range(sample_data, "2024-01-01", "2024-01-15")
    assert len(result) == 1
    assert result[0]["description"] == "Ozon"


def test_count_by_category():
    result = count_by_category(sample_data)
    assert result["Ozon"] == 1
    assert result["M.Video"] == 1
