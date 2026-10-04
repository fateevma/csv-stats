
import pytest

from csvstats.core import Stats, compute_stats


def test_compute_stats_basic():
    assert compute_stats([10, 20, 30]) == Stats(count=3, minimum=10, maximum=30, mean=20, total=60)


def test_compute_stats_one_value():
    stats = compute_stats([5.5])
    assert stats.minimum == stats.maximum == stats.mean == 5.5


def test_compute_stats_empty():
    with pytest.raises(ValueError, match="Нет числовых значений"):
        compute_stats([])


