# Bank Transactions CLI

CLI-приложение для анализа банковских транзакций из Excel-файла.

## 🔧 Возможности
- Загрузка транзакций из Excel (`.xlsx`)
- Фильтрация по дате, валюте, статусу, ключевым словам
- Сводка по категориям
- Поддержка .env и пользовательских настроек

## 🗂️ Структура проекта
.
├── src/ # Исходный код приложения
├── data/ # Excel-файл с транзакциями
├── tests/ # Автотесты
├── .env # Переменные окружения
├── .env_template # Шаблон .env
├── user_settings.json # Настройки пользователя
├── pyproject.toml # Poetry-конфигурация

## 🚀 Запуск

```bash
poetry install
poetry run python src/main.py --status EXECUTED --summary

poetry run pytest

## 📦 Используемые технологии
Python 3.10+

pandas, openpyxl

poetry, pytest, dotenv, ruff, mypy

yaml
Копировать
Редактировать

---

## ✅ 2. `.env`

```env
DATA_PATH=data/operations.xlsx
