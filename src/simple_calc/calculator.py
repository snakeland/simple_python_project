"""Simple calculator module

Provides basic arithmetic functions and small input validation.
"""

Number = int | float


def add(a: Number, b: Number) -> Number:
    """Return a + b"""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return a - b"""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return a * b"""
    return a * b


def divide(a: Number, b: Number) -> Number:
    """Return a / b. Raises ValueError on divide-by-zero."""
    if b == 0:
        raise ValueError("division by zero")
    return a / b


def average(*numbers: Number) -> float:
    """Return the arithmetic mean of the given numbers.

    Args:
        *numbers: Variable number of int or float values

    Returns:
        The arithmetic mean as a float

    Raises:
        ValueError: If no numbers are provided
    """
    if not numbers:
        raise ValueError("average requires at least one number")
    return sum(numbers) / len(numbers)
