#!/usr/bin/env python3
"""Thin wrapper delegating to the package CLI.

Usage: python bin/run_calc.py <op> <num1> <num2>
This simply forwards to `simple_calc.cli:main` so behavior matches `run-calc`.
"""
import sys
import os

try:
    from simple_calc.cli import main as _main
except ModuleNotFoundError:
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    src_path = os.path.join(repo_root, "src")
    if src_path not in sys.path:
        sys.path.insert(0, src_path)
    from simple_calc.cli import main as _main


if __name__ == "__main__":
    _main(sys.argv[1:])
