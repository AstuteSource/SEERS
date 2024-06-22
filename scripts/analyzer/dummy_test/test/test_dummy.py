"""Test suite to ensure that each function words correctly."""

from src import __version__
from src import main


def test_version():
    """Confirm that the version of the program is correct."""
    assert __version__ == "0.1.0"