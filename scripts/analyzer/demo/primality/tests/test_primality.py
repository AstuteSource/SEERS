"""Test suite to ensure that each function words correctly."""

from src import __version__
from src import main


def test_version():
    """Confirm that the version of the program is correct."""
    assert __version__ == "0.1.0"


def test_exhaustive_primality_prime_number():
    """Confirm that a primality testing function can detect a prime number."""
    # exhaustive method testing number 104729
    # set a tuple variable that contains the return
    primality_tuple = main.primality_test_exhaustive(104729)
    # result contains 2 parts, primality_tuple[0] as bool (True or False)
    was_prime_found = primality_tuple[0]
    # result contains primality_tuple[1] which is the divisor_list
    divisor_list = primality_tuple[1]
    assert was_prime_found is True
    # asset that the divisor_list holds 2 values
    assert len(divisor_list) == 2


def test_exhaustive_primality_not_prime_number():
    """Confirm that a primality testing function can detect a prime number."""
    primality_tuple = main.primality_test_exhaustive(27)
    was_prime_found = primality_tuple[0]
    divisor_list = primality_tuple[1]
    assert was_prime_found is False
    # if the number is not prime, list should only return smallest divisor
    assert len(divisor_list) == 1


def test_efficient_primality_prime_number():
    """Confirm that a primality testing function can detect a prime number."""
    primality_tuple = main.primality_test_efficient(104729)
    was_prime_found = primality_tuple[0]
    divisor_list = primality_tuple[1]
    assert was_prime_found is True
    assert len(divisor_list) == 2


def test_efficient_primality_not_prime_number():
    """Confirm that a primality testing function can detect a prime number."""
    primality_tuple = main.primality_test_efficient(27)
    was_prime_found = primality_tuple[0]
    divisor_list = primality_tuple[1]
    assert was_prime_found is False
    assert len(divisor_list) == 1
