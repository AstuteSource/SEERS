"""Compute values in the Fibonacci sequence using different approaches."""

# Import all of the needed type annotations
from typing import List
from typing import Tuple

#  Refer to the course slides for more details about how to
# implement these functions

# Refer to your results from running experiments as part of a
# previous engineering effort to develop working hypotheses about the
# performance characteristics of these functions


def fibonacci_recursivelist(number: int) -> List[int]:
    """Start with 0 and compute up to and include the number-th Fibonacci number using recursion and a list."""
    if number == 0 or number == 1:
        return [0, 1]
    if number == 2:
        return [0, 1, 1]
    list = fibonacci_recursivelist(number - 1)
    list.append(list[-1] + list[-2])
    return list

    # Reference:
    # https://stackoverflow.com/questions/33325683/python-creating-a-list-of-the-first-n-fibonacci-numbers
    # Base case: return [0, 1] when number is either 0 or 1
    # Recursive case: perform the computation for number - 1 and
    # then append to the list the two previous computations added together
    # Finally, return the current version of the list.


def fibonacci_recursivetuple(number: int) -> Tuple[int, ...]:
    """Start with 0 and compute up to and include the number-th Fibonacci number using recursion and a list."""
    # Base case: return [0,1] when number is either 0 or 1
    if number == 0 or number == 1:
        return (0, 1)
    if number == 2:
        return (0, 1, 1)
    tuple = fibonacci_iterativetuple(number - 1)
    result = tuple[-1] + tuple[-2]
    tuple += (result,)
    return tuple
    # Reference:
    # https://stackoverflow.com/questions/33325683/python-creating-a-list-of-the-first-n-fibonacci-numbers
    # Note that the reference describes the computation for lists and not tuples
    # Base case: return [0, 1] when number is either 0 or 1
    # Recursive case: perform the computation for number - 1 and
    # then "append" to the tuple the two previous computations added together,
    # bearing in mind that the use of += will create a new tuple.
    # Finally, return the current version of the tuple.


def fibonacci_iterativetuple(number: int) -> Tuple[int, ...]:
    """Start with 0 and compute up to and including the number-th Fibonacci number using iteration and a tuple."""
    # create an empty tuple that will ultimately contain the results
    tuple_: Tuple[int, ...] = ()
    # set the initial conditions of the sequence
    # Note: start at 0 and 1, not at 1 and 1 like in the course slides
    # Note: different start is to ensure consistency with this article:
    # https://realpython.com/fibonacci-sequence-python/
    a = 0
    b = 1
    for i in range(number + 1):
        # iterate from zero to the (number)th number
        # --> store the value of a in the tuple
        # --> move to the next value such that:
        # --> a gets the current value of b
        # --> b gets the current value of a + b
        tuple_ += (a,)
        # simultaneously assign value to pair
        a, b = b, a + b
    return tuple_
    # return the final tuple that contains the fibonacci numbers


def fibonacci_iterativelist(number: int) -> List[int]:
    """Start with 0 and compute up to and including the number-th Fibonacci number using a list."""
    # create an empty list that will ultimately contain the results
    list = []
    # set the initial conditions of the sequence
    # Note: start at 0 and 1, not at 1 and 1 like in the course slides
    # Note: different start is to ensure consistency with this article:
    # https://realpython.com/fibonacci-sequence-python/
    a = 0
    b = 1
    # set the initial conditions of the sequence
    # iterate from zero to the (number)th number
    # --> store the value of a in the list
    # --> move to the next value such that:
    # -->a gets the current value of b
    # --> b gets the current value of a + b
    # return the final tuple that contains the fibonacci numbers
    for i in range(number):
        list.append(a)
        a, b = b, a + b
    return list
