#!/usr/bin/env python3
"""Tiny CLI wrapper to call calculator functions.

Usage: python bin/run_calc.py <op> <num1> <num2>
Where <op> is one of: add, subtract, multiply, divide
"""
#!/usr/bin/env python3
"""Backwards-compatible thin wrapper CLI.

It delegates to the installed package entrypoint `simple_calc.cli:main` when
the package is not executed as a script directly.
"""
import sys
from simple_calc.cli import main as _main

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
    # Delegate to the package CLI implementation for consistent behavior
    _main(sys.argv[1:])
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
