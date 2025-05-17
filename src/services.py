from datetime import datetime
from typing import Any


def filter_by_status(data: list[dict[str, Any]], status: str) -> list[dict[str, Any]]:
    """Фильтрация по статусу (например, EXECUTED)."""
    return [item for item in data if item.get("status") == status]


def filter_by_date_range(data: list[dict[str, Any]], start: str, end: str) -> list[dict[str, Any]]:
    """Фильтрация по диапазону дат."""
    try:
        start_date = datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")
    except ValueError as e:
        raise ValueError(f"Неверный формат даты: {e}")

    return [
        item for item in data
        if "date" in item and start_date <= datetime.fromisoformat(item["date"]) <= end_date
    ]


def filter_by_currency(data: list[dict[str, Any]], currency: str) -> list[dict[str, Any]]:
    """Фильтрация по валюте (например, USD)."""
    return [
        item for item in data
        if item.get("operationAmount", {}).get("currency", {}).get("code") == currency
    ]


def filter_by_keyword(data: list[dict[str, Any]], keyword: str) -> list[dict[str, Any]]:
    """Фильтрация по ключевому слову в описании."""
    return [
        item for item in data
        if keyword.lower() in item.get("description", "").lower()
    ]


def count_by_category(data: list[dict[str, Any]]) -> dict[str, int]:
    """Подсчёт количества операций по категориям (description)."""
    result: dict[str, int] = {}
    for item in data:
        description = item.get("description", "Неизвестно")
        result[description] = result.get(description, 0) + 1
    return result
