
import pytest

from csvstats.core import Stats, compute_stats
from csvstats.core import parse_number
from csvstats.core import Stats
from csvstats.core import CollumnNotFoundError, read_column

def test_compute_stats_basic():
    assert compute_stats([10, 20, 30]) == Stats(count=3, minimum=10, maximum=30, mean=20, total=60)


def test_compute_stats_one_value():
    stats = compute_stats([5.5])
    assert stats.minimum == stats.maximum == stats.mean == 5.5


def test_compute_stats_empty():
    with pytest.raises(ValueError, match="Нет числовых значений"):
        compute_stats([])

@pytest.mark.parametrize(
    ("text", "expected_output"),
    [
        ("42", 42.0),
        ("3.14", 3.14),
        ("-7", -7.0),
        ("0", 0.0),
        ("not_a_number", None),
        ("", None),
    ],
)
def test_parse_number(text, expected_output):
    assert parse_number(text) == expected_output

@pytest.fixture
def csv_file(tmp_path):
    file= tmp_path / "sales.csv"
    file.write_text("product,price\nЧай,120\nСок,\nТорт,950\n", encoding="utf-8")
    return file

def test_read_column_valid(csv_file):
    assert list(read_column(csv_file, "price")) == ["120", "", "950"]

def test_read_column_missing(csv_file):
    with pytest.raises(CollumnNotFoundError, match="qty"):
        list(read_column(csv_file, "qty"))  