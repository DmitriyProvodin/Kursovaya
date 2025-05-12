from load_data import load_transactions_from_excel
from filters import (
    filter_by_date_range,
    filter_by_category,
    filter_by_currency,
    filter_by_description_keyword,
)
from export import export_to_json, export_to_excel
import os

EXCEL_PATH = "operations.xlsx"
EXPORT_DIR = "reports"


def main():
    # Создание папки reports, если не существует
    os.makedirs(EXPORT_DIR, exist_ok=True)

    # Загрузка данных
    df = load_transactions_from_excel(EXCEL_PATH)
    if df.empty:
        print("❌ Не удалось загрузить данные.")
        return

    print("✅ Загружено операций:", len(df))

    # Выбор фильтрации
    print("\nВыберите фильтр:")
    print("1. По дате")
    print("2. По категории")
    print("3. По валюте")
    print("4. По описанию")
    print("5. Без фильтра — экспорт всех OK-операций")
    choice = input("Введите номер: ")

    if choice == "1":
        start = input("Введите начальную дату (YYYY-MM-DD): ")
        end = input("Введите конечную дату (YYYY-MM-DD): ")
        df = filter_by_date_range(df, start, end)
    elif choice == "2":
        cat = input("Введите категорию (например, Супермаркеты): ")
        df = filter_by_category(df, cat)
    elif choice == "3":
        cur = input("Введите валюту (например, RUB): ")
        df = filter_by_currency(df, cur)
    elif choice == "4":
        keyword = input("Введите ключевое слово (например, Ozon): ")
        df = filter_by_description_keyword(df, keyword)

    if df.empty:
        print("⚠️ Нет транзакций после фильтрации.")
        return

    # Экспорт
    json_path = os.path.join(EXPORT_DIR, "filtered_transactions.json")
    xlsx_path = os.path.join(EXPORT_DIR, "filtered_transactions.xlsx")
    export_to_json(df, json_path)
    export_to_excel(df, xlsx_path)


if __name__ == "__main__":
    main()

