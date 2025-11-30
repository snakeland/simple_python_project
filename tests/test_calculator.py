import os
import sys

import pytest

# Make the src/ directory importable so tests can import the package
HERE = os.path.dirname(__file__)
SRC = os.path.abspath(os.path.join(HERE, "..", "src"))
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from simple_calc.calculator import add, average, divide, multiply, subtract  # noqa: E402


def test_add():
    assert add(1, 2) == 3
    assert add(1.5, 2.25) == 3.75


def test_subtract():
    assert subtract(10, 3) == 7
    assert subtract(1.5, 0.5) == 1.0


def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(2.5, 2) == 5.0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_average_two_numbers():
    assert average(10, 20) == 15.0
    assert average(1.5, 2.5) == 2.0


def test_average_multiple_numbers():
    assert average(1, 2, 3, 4, 5) == 3.0
    assert average(10, 20, 30) == 20.0


def test_average_single_number():
    assert average(42) == 42.0


def test_average_mixed_types():
    assert average(1, 2.5, 3) == 2.1666666666666665
    assert average(10, 15.0, 20) == 15.0


def test_average_negative_numbers():
    assert average(-10, 10) == 0.0
    assert average(-5, -10, -15) == -10.0


def test_average_no_numbers():
    with pytest.raises(ValueError, match="average requires at least one number"):
        average()
