import pandas as pd


def export_to_json(df: pd.DataFrame, path: str) -> None:
    """
    Сохраняет DataFrame в JSON-файл.

    :param df: DataFrame с транзакциями.
    :param path: Путь к файлу JSON.
    """
    try:
        df.to_json(path, orient="records", force_ascii=False, indent=4, date_format="iso")
        print(f"✅ JSON успешно сохранён в {path}")
    except Exception as e:
        print(f"❌ Ошибка при сохранении JSON: {e}")


def export_to_excel(df: pd.DataFrame, path: str) -> None:
    """
    Сохраняет DataFrame в Excel-файл.

    :param df: DataFrame с транзакциями.
    :param path: Путь к файлу Excel.
    """
    try:
        df.to_excel(path, index=False)
        print(f"✅ Excel успешно сохранён в {path}")
    except Exception as e:
        print(f"❌ Ошибка при сохранении Excel: {e}")
