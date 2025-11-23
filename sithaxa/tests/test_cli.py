# Test for sithaxa/cli/main.py
import pytest
from typer.testing import CliRunner

from sithaxa.cli.main import app
runner = CliRunner()
def test_hello_command():
    result = runner.invoke(app, ["hello", "greet", "World"])
    assert result.exit_code == 0
    assert "👋 Hello, World! Welcome to Sithaxa." in result.output
