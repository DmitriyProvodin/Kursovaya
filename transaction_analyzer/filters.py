import pandas as pd


def filter_by_date_range(df: pd.DataFrame, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Фильтрует транзакции по диапазону дат.

    :param df: DataFrame с транзакциями.
    :param start_date: Начальная дата в формате 'YYYY-MM-DD'.
    :param end_date: Конечная дата в формате 'YYYY-MM-DD'.
    :return: Отфильтрованный DataFrame.
    """
    mask = (df['Дата операции'] >= pd.to_datetime(start_date)) & (df['Дата операции'] <= pd.to_datetime(end_date))
    return df[mask].copy()


def filter_by_category(df: pd.DataFrame, category: str) -> pd.DataFrame:
    """
    Фильтрует транзакции по категории.

    :param df: DataFrame с транзакциями.
    :param category: Название категории (например, 'Супермаркеты').
    :return: Отфильтрованный DataFrame.
    """
    return df[df['Категория'] == category].copy()


def filter_by_currency(df: pd.DataFrame, currency: str) -> pd.DataFrame:
    """
    Фильтрует транзакции по валюте операции.

    :param df: DataFrame с транзакциями.
    :param currency: Код валюты (например, 'RUB', 'USD').
    :return: Отфильтрованный DataFrame.
    """
    return df[df['Валюта операции'] == currency].copy()


def filter_by_description_keyword(df: pd.DataFrame, keyword: str) -> pd.DataFrame:
    """
    Фильтрует транзакции по ключевому слову в описании.

    :param df: DataFrame с транзакциями.
    :param keyword: Ключевое слово (например, 'Ozon').
    :return: Отфильтрованный DataFrame.
    """
    return df[df['Описание'].str.contains(keyword, case=False, na=False)].copy()
