#!/usr/bin/env python3
"""Tiny CLI wrapper to call calculator functions.

Usage: python bin/run_calc.py <op> <num1> <num2>
Where <op> is one of: add, subtract, multiply, divide
"""
import sys
from simple_calc import add, subtract, multiply, divide

OPS = {
    "add": add,
    "subtract": subtract,
    "mul": multiply,
    "multiply": multiply,
    "div": divide,
    "divide": divide,
}


def usage():
    print("Usage: run_calc.py <op> <num1> <num2>")
    print("ops: add, subtract, multiply (or mul), divide (or div)")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage()
        sys.exit(2)

    op, a_str, b_str = sys.argv[1:4]
    try:
        a = float(a_str) if ('.' in a_str or 'e' in a_str.lower()) else int(a_str)
        b = float(b_str) if ('.' in b_str or 'e' in b_str.lower()) else int(b_str)
    except ValueError:
        print("Error: num1 and num2 must be numbers")
        sys.exit(2)

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
