import json
import pandas as pd
from typing import Any


def load_data(file_path: str) -> list[dict[str, Any]]:
    """
    Загружает данные из XLSX-файла и преобразует их в список словарей.
    :param file_path: Путь к файлу Excel.
    :return: Список словарей с транзакциями.
    """
    try:
        df = pd.read_excel(file_path)
        # Убираем строки с полностью пустыми значениями
        df.dropna(how="all", inplace=True)
        # Преобразуем DataFrame в список словарей
        return df.to_dict(orient="records")
    except Exception as e:
        raise RuntimeError(f"Ошибка при загрузке файла: {e}")
