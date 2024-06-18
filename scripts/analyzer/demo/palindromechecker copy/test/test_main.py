"""Test suite to ensure that each function works correctly."""

from typer.testing import CliRunner

from src.main import cli

# Add comments to the test cases to explain how the tests works

runner = CliRunner()
# Review how runner.invoke works by reading the documentation
# Reference:
# https://typer.tiangolo.com/tutorial/testing/


def test_palindromechecker_recursive_is_palindrome():
    """Ensure that the command-line interface works for recursive approach."""
    # invoke() method of the `runner` object is called with the cli arguments
    result = runner.invoke(cli, ["--word", "civic", "--approach", "recursive"])
    # checks whether the program exited without errors
    assert result.exit_code == 0
    # assert Recursive in program output
    assert "recursive" in result.stdout
    assert "reverse" not in result.stdout
    # assert True in human_readable_boolean
    assert "Yes, it is!" in result.stdout
    # assert the word in the program output
    assert "civic" in result.stdout


def test_palindromechecker_recursive_is_not_palindrome():
    """Ensure that the command-line interface works for recursive approach."""
    result = runner.invoke(cli, ["--word", "love", "--approach", "recursive"])
    assert result.exit_code == 0
    assert "recursive" in result.stdout
    assert "reverse" not in result.stdout
    assert "No, it is not" in result.stdout
    assert "love" in result.stdout


def test_palindromechecker_reverse_is_palindrome():
    """Ensure that the command-line interface works for reverse approach."""
    result = runner.invoke(cli, ["--word", "civic", "--approach", "reverse"])
    # checks whether the program exited without errors
    assert result.exit_code == 0
    # assert Recursive in program output
    assert "reverse" in result.stdout
    assert "recursive" not in result.stdout
    # assert True in human_readable_boolean
    assert "Yes, it is!" in result.stdout
    # assert the word in the program output
    assert "civic" in result.stdout


def test_palindromechecker_reverse_is_not_palindrome():
    """Ensure that the command-line interface works for reverse approach."""
    result = runner.invoke(cli, ["--word", "love", "--approach", "reverse"])
    assert result.exit_code == 0
    assert "reverse" in result.stdout
    assert "recursive" not in result.stdout
    assert "No, it is not" in result.stdout
    assert "love" in result.stdout
