
import pytest

from csvstats.core import Stats, compute_stats
from csvstats.core import parse_number
from csvstats.core import Stats

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
