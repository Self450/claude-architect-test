import pytest
from src.calculator import fibonacci


@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (6, 8),
    (10, 55),
    (20, 6765),
])
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected


def test_fibonacci_negative_raises():
    with pytest.raises(ValueError):
        fibonacci(-1)
