import re

import simple_calc.cli as cli

# Helper to call main without exiting the interpreter


def invoke(args):
    return cli.main(args, exit_process=False)


def test_cli_add(capsys):
    code = invoke(["add", "2", "3"])
    assert code == 0
    out = capsys.readouterr().out.strip()
    assert out == "5"


def test_cli_alias_mul(capsys):
    code = invoke(["mul", "2", "4"])
    assert code == 0
    out = capsys.readouterr().out.strip()
    assert out == "8"


def test_cli_non_numeric(capsys):
    code = invoke(["add", "x", "3"])
    assert code == 2
    out = capsys.readouterr().out
    assert "Error:" in out
    assert "numbers" in out


def test_cli_unknown_op(capsys):
    code = invoke(["pow", "2", "3"])
    assert code == 2
    out = capsys.readouterr().out
    assert "Unknown operation" in out
    assert "Usage:" in out


def test_cli_arg_count(capsys):
    code = invoke(["add", "2"])  # missing one arg
    assert code == 2
    out = capsys.readouterr().out
    assert "Usage:" in out


def test_cli_divide_by_zero(capsys):
    code = invoke(["divide", "5", "0"])
    assert code == 1
    out = capsys.readouterr().out
    assert re.search(r"Error: division by zero", out)


def test_cli_scientific_notation(capsys):
    code = invoke(["add", "1e2", "50"])
    assert code == 0
    out = capsys.readouterr().out.strip()
    assert out == "150.0"


def test_cli_average_two_numbers(capsys):
    code = invoke(["average", "10", "20"])
    assert code == 0
    out = capsys.readouterr().out.strip()
    assert out == "15.0"


def test_cli_average_multiple_numbers(capsys):
    code = invoke(["avg", "1", "2", "3", "4", "5"])
    assert code == 0
    out = capsys.readouterr().out.strip()
    assert out == "3.0"


def test_cli_average_single_number(capsys):
    code = invoke(["average", "42"])
    assert code == 0
    out = capsys.readouterr().out.strip()
    assert out == "42.0"


def test_cli_average_no_numbers(capsys):
    code = invoke(["average"])
    assert code == 2
    out = capsys.readouterr().out
    assert "Usage:" in out


def test_cli_binary_op_wrong_arg_count(capsys):
    code = invoke(["add", "1", "2", "3"])
    assert code == 2
    out = capsys.readouterr().out
    assert "requires exactly 2 numbers" in out
