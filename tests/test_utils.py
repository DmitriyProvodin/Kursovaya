from src.utils import load_data
import pandas as pd


def test_load_data(tmp_path):
    # Создаём временный Excel-файл
    test_data = pd.DataFrame([
        {"description": "Покупка", "operationAmount": {"amount": 100, "currency": {"code": "RUB"}}}
    ])
    file_path = tmp_path / "test.xlsx"
    test_data.to_excel(file_path, index=False)

    result = load_data(str(file_path))
    assert isinstance(result, list)
    assert result[0]["description"] == "Покупка"
