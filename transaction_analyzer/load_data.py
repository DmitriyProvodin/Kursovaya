import pandas as pd
from typing import Optional


def load_transactions_from_excel(path: str) -> pd.DataFrame:
    """
    Загружает транзакции из Excel-файла и возвращает DataFrame с успешными операциями.

    :param path: Путь к Excel-файлу.
    :return: DataFrame с транзакциями, прошедшими фильтр по статусу "OK".
    """
    try:
        df = pd.read_excel(path, sheet_name=0)

        # Преобразование даты
        df['Дата операции'] = pd.to_datetime(df['Дата операции'], errors='coerce')

        # Приведение числовых столбцов
        df['Сумма операции'] = pd.to_numeric(df['Сумма операции'], errors='coerce')
        df['Валюта операции'] = df['Валюта операции'].astype(str)

        # Фильтрация только по успешным операциям
        df = df[df['Статус'] == 'OK'].copy()

        # Сброс индексов
        df.reset_index(drop=True, inplace=True)

        return df

    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
        return pd.DataFrame()  # Возвращаем пустой DataFrame при ошибке
