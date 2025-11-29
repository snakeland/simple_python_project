"""Simple calculator module

Provides four basic arithmetic functions and small input validation.
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
