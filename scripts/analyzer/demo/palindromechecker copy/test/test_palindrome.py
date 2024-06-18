"""Test cases for palindrome functions."""

from src.palindrome import is_palindrome_recursive
from src.palindrome import is_palindrome_reverse


# test case for recursive approach, return the result True
def test_short_palindrome_word_recursive():
    """Ensure that a short word of "civic" works correctly with recursive."""
    # give the function a palindrome word
    word = "civic"
    # calling the function from the palindrome.py
    result = is_palindrome_recursive(word)
    # assert the result
    assert result is True


def test_short_not_palindrome_word_recursive():
    """Ensure that a short word of "taylor" does not work correctly with recursive."""
    word = "taylor"
    result = is_palindrome_recursive(word)
    assert result is False


def test_short_palindrome_word_reverse():
    """Ensure that a short word of "civic" works correctly with reverse."""
    word = "civic"
    result = is_palindrome_reverse(word)
    assert result is True


def test_short_not_palindrome_word_reverse():
    """Ensure that a short word of "taylor" does not work correctly with reverse."""
    word = "taylor"
    result = is_palindrome_reverse(word)
    assert result is False
