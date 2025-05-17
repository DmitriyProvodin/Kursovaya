from typing import Any


def print_transactions(data: list[dict[str, Any]]) -> None:
    """Печать информации о транзакциях."""
    if not data:
        print("Нет данных для отображения.")
        return

    for item in data:
        date = item.get("date", "—")[:10]
        description = item.get("description", "Нет описания")
        amount = item.get("operationAmount", {}).get("amount", "0")
        currency = item.get("operationAmount", {}).get("currency", {}).get("code", "")
        print(f"{date} | {description} | {amount} {currency}")
    print(f"\nВсего операций: {len(data)}")


def print_summary(summary: dict[str, int]) -> None:
    """Печать сводки по категориям."""
    if not summary:
        print("Нет данных для сводки.")
        return

    print("\nСводка по категориям:")
    for category, count in summary.items():
        print(f"{category}: {count}")
