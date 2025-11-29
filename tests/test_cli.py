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
