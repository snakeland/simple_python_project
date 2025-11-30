#!/usr/bin/env python3
"""CLI entrypoint for simple_calc package.

Delegates to the same logic used by bin/run_calc.py so the project can be
installed with a console script named `run-calc`.
"""

import sys

from .calculator import add, average, divide, multiply, subtract

OPS = {
    "add": add,
    "subtract": subtract,
    "mul": multiply,
    "multiply": multiply,
    "div": divide,
    "divide": divide,
    "average": average,
    "avg": average,
}


def usage():
    print("Usage: run-calc <op> <num1> [num2] [num3...]")
    print("Binary ops: add, subtract, multiply (or mul), divide (or div)")
    print("Variadic ops: average (or avg)")


def parse_number(s: str):
    try:
        return float(s) if ("." in s or "e" in s.lower()) else int(s)
    except ValueError as err:
        raise ValueError("num1 and num2 must be numbers") from err


def run(argv):
    """Core CLI logic.

    Returns an integer exit code and prints output/messages.
    Exit codes: 0 success, 1 operation error, 2 usage/argument error.
    """
    if len(argv) < 2:
        usage()
        return 2

    op = argv[0]
    num_strs = argv[1:]

    try:
        numbers = [parse_number(s) for s in num_strs]
    except ValueError as e:
        print(f"Error: {e}")
        return 2

    fn = OPS.get(op)
    if fn is None:
        print(f"Unknown operation: {op}")
        usage()
        return 2

    # Check argument count for binary operations
    if fn in (add, subtract, multiply, divide) and len(numbers) != 2:
        print(f"Error: {op} requires exactly 2 numbers")
        usage()
        return 2

    try:
        result = fn(*numbers)
    except Exception as e:
        print(f"Error: {e}")
        return 1

    print(result)
    return 0


def main(argv=None, exit_process=True):
    argv = argv if argv is not None else sys.argv[1:]
    code = run(argv)
    if exit_process:
        sys.exit(code)  # pragma: no cover
    return code


if __name__ == "__main__":  # pragma: no cover
    main()  # pragma: no cover
