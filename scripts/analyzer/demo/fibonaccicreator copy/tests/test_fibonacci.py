"""Add test cases for the functions in the fibonacci module."""


import sympy

from src import fibonacci


# testing iterative tuple with an input of 0, asset output tuple to have 1 digit (0,)
def test_zeroth_fibonacci_empty_tuple():
    """Ensure that the request for the zeroth Fibonacci number returns empty tuple."""
    number = 0
    result = fibonacci.fibonacci_iterativetuple(number)
    assert len(result) == 1
    assert result == (0,)


# testing iterative tuple with input 1, asset output (0,1,)
def test_first_fibonacci_singleton_tuple():
    """Ensure that the request for first Fibonacci number returns same number in a tuple."""
    number = 1
    result = fibonacci.fibonacci_iterativetuple(number)
    assert len(result) == number + 1
    assert result == (
        0,
        1,
    )
    assert sympy.fibonacci(1) == result[-1]


# testing iterativetuple with input 2, assert output (0,1,1)
def test_second_fibonacci_tuple():
    """Ensure that the request for the second Fibonacci number returns same number twice in a tuple."""
    number = 2
    result = fibonacci.fibonacci_iterativetuple(number)
    assert len(result) == number + 1
    assert result == (0, 1, 1)
    assert sympy.fibonacci(2) == result[-1]


# testing iterative tuple with input 10, assert output a tuple with 11 digits
def test_tenth_fibonacci_tuple():
    """Ensure that the request for the tenth Fibonacci number returns the correct tuple of numbers."""
    number = 10
    result = fibonacci.fibonacci_iterativetuple(number)
    assert len(result) == number + 1
    assert result == (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55)
    assert sympy.fibonacci(10) == result[-1]


# testing function with input 50, output a tuple with 51 digits
def test_fiftieth_fibonacci_tuple():
    """Ensure that the request for the 50th Fibonacci number is correct according to sympy function."""
    number = 50
    result = fibonacci.fibonacci_iterativetuple(number)
    assert len(result) == number + 1
    assert sympy.fibonacci(50) == result[-1]
