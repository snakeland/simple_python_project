#!/usr/bin/env python3
"""CLI entrypoint for simple_calc package.

Delegates to the same logic used by bin/run_calc.py so the project can be
installed with a console script named `run-calc`.
"""
import sys

from .calculator import add, subtract, multiply, divide

OPS = {
    "add": add,
    "subtract": subtract,
    "mul": multiply,
    "multiply": multiply,
    "div": divide,
    "divide": divide,
}


def usage():
    print("Usage: run-calc <op> <num1> <num2>")
    print("ops: add, subtract, multiply (or mul), divide (or div)")


def parse_number(s: str):
    try:
        return float(s) if ('.' in s or 'e' in s.lower()) else int(s)
    except ValueError:
        raise ValueError("num1 and num2 must be numbers")


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) != 3:
        usage()
        sys.exit(2)

    op, a_str, b_str = argv
    a = parse_number(a_str)
    b = parse_number(b_str)

    fn = OPS.get(op)
    if fn is None:
        print(f"Unknown operation: {op}")
        usage()
        sys.exit(2)

    try:
        result = fn(a, b)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(result)


if __name__ == "__main__":
    main()
