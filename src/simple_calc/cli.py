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


def run(argv):
    """Core CLI logic.

    Returns an integer exit code and prints output/messages.
    Exit codes: 0 success, 1 operation error, 2 usage/argument error.
    """
    if len(argv) != 3:
        usage()
        return 2

    op, a_str, b_str = argv
    try:
        a = parse_number(a_str)
        b = parse_number(b_str)
    except ValueError as e:
        print(f"Error: {e}")
        return 2

    fn = OPS.get(op)
    if fn is None:
        print(f"Unknown operation: {op}")
        usage()
        return 2

    try:
        result = fn(a, b)
    except Exception as e:
        print(f"Error: {e}")
        return 1

    print(result)
    return 0


def main(argv=None, exit_process=True):
    argv = argv if argv is not None else sys.argv[1:]
    code = run(argv)
    if exit_process:
        sys.exit(code)
    return code


if __name__ == "__main__":
    main()
