import csv
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path


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

class CollumnNotFoundError(ValueError):
    """Исключение, которое выбрасывается, если не найден столбец в CSV файле"""

def read_column(path: str | Path, column: str) -> Iterator[str]:
    """Читает столбец из CSV файла и возвращает список чисел"""
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        if column not in headers:
            raise CollumnNotFoundError(f"колонка {column} не найден. Есть: {', '.join(headers)}")
        for row in reader:
            yield row[column]
 