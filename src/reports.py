import json
from typing import Any

def generate_json_report(data: Any, path: str) -> None:
    """Сохраняет отчёт в JSON-файл."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
