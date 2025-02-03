from pathlib import Path
from unittest.mock import patch

import pandas

from config import ROOT_DIR
from src.read_table import read_csv, read_xlsx


@patch("csv.DictReader")
def test_read_csv(mock_reader_csv):
    mock_reader_csv.return_value = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    csv_path = Path.joinpath(ROOT_DIR, "data", "transactions.csv")
    result = read_csv(csv_path)
    expected = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    assert result == expected
    with open(csv_path, "r"):
        mock_reader_csv.assert_called_once()


@patch("pandas.read_excel")
def test_read_xlsx(mock_reader_xlsx):
    mock_reader_xlsx.return_value = pandas.DataFrame({"a": {"a": 1, "b": 2}, "b": {"a": 3, "b": 4}})
    xlsx_path = Path.joinpath(ROOT_DIR, "data", "transactions_excel.xlsx")
    result = read_xlsx(xlsx_path)
    expected = [{"a": 1, "b": 3}, {"a": 2, "b": 4}]
    assert result == expected
    mock_reader_xlsx.assert_called_once()
