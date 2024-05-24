"""Test suits for util module."""

from src.util import human_readable_boolean


def test_human_readable_boolean_true():
    """Ensure that a human-readable true boolean works correctly."""
    # given the boolean value
    true_value = True
    # call function with the given value
    true_value_human_readable = human_readable_boolean(true_value)
    # assert output
    # to test if actual output === expected output
    assert true_value_human_readable == "Yes, it is!"


def test_human_readable_boolean_false():
    """Ensure that a human-readable false boolean works correctly."""
    true_value = False
    true_value_human_readable = human_readable_boolean(true_value)
    assert true_value_human_readable == "No, it is not!"
