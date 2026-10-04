from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(frozen=True)
class Stats:
    count: int
    mean: float
    minimum: float
    maximum: float
    total: float

def compute_stats(value: Iterable[float]) -> Stats:
    data = list(value)
    if not data:
        raise ValueError("Нет числовых значений")
    total = sum(data)
    return Stats(
        count=len(data),
        minimum=min(data),
        maximum=max(data),
        mean=round(total / len(data), 2),
        total=total,
    )
def parse_number(text: str) -> float | None:
    """Превращает строку в число. Если не получилось - Возвращает None"""
    try:
        return float(text.strip())
    except ValueError:
        return None



