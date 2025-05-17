import os
import argparse
from dotenv import load_dotenv
from src.utils import load_data
from src.services import (
    filter_by_status,
    filter_by_date_range,
    filter_by_currency,
    filter_by_keyword,
    count_by_category,
)
from src.views import print_transactions, print_summary

# Загрузка переменных окружения
load_dotenv()

# Путь к файлу по умолчанию
DATA_PATH = os.getenv("DATA_PATH", "data/operations.xlsx")


def main() -> None:
    # Настройка CLI
    parser = argparse.ArgumentParser(description="Анализатор банковских транзакций")
    parser.add_argument("--status", help="Фильтр по статусу (например, EXECUTED)")
    parser.add_argument("--start", help="Начальная дата (ГГГГ-ММ-ДД)")
    parser.add_argument("--end", help="Конечная дата (ГГГГ-ММ-ДД)")
    parser.add_argument("--currency", help="Фильтр по валюте (например, USD)")
    parser.add_argument("--keyword", help="Фильтр по ключевому слову в описании")
    parser.add_argument("--summary", action="store_true", help="Показать сводку по категориям")
    args = parser.parse_args()

    # Загрузка данных
    transactions = load_data(DATA_PATH)

    # Применение фильтров
    if args.status:
        transactions = filter_by_status(transactions, args.status)
    if args.start and args.end:
        transactions = filter_by_date_range(transactions, args.start, args.end)
    if args.currency:
        transactions = filter_by_currency(transactions, args.currency)
    if args.keyword:
        transactions = filter_by_keyword(transactions, args.keyword)

    # Печать результатов
    print_transactions(transactions)

    # Печать сводки, если указано
    if args.summary:
        summary = count_by_category(transactions)
        print_summary(summary)


if __name__ == "__main__":
    main()
