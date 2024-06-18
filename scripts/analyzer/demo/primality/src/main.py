"""Perform primality testing with both exhaustive and efficient approaches."""


from enum import Enum
from typing import Iterable
from typing import List
from typing import Tuple

import typer
from pyinstrument import Profiler
from rich.console import Console

# this line imports the 'Tuple' and 'List' from the 'typing' module, which provides support for type annotations in Python.


# create a Typer object to support the command-line interface
cli = typer.Typer()
# create a Profiler object to support timing program code segments
profiler = Profiler()


class PrimalityTestingApproach(str, Enum):
    """Define the name for the approach for performing primality testing."""

    EXHAUSTIVE = "exhaustive"
    EFFICIENT = "efficient"


def human_readable_boolean(answer: bool) -> str:
    """Produce a human-readable Yes or No for a boolean value of True or False."""
    if answer:
        return "Yes"
    return "No"


def pretty_print_list(values: Iterable[int]) -> str:
    """Pretty print a list without brackets and adding commas."""
    # create an empty list
    result = []
    # use for string to convert each value to string and add to list
    for value in values:
        result.append(str(value))
    # separate each value by a comma by using the join method
    return ",".join(result)


# define the function which taks an integer 'number' as unput and returns a tuple of two values: a boolean and a list of integers
def primality_test_exhaustive(number: int) -> Tuple[bool, List[int]]:
    """Perform an exhaustive primality test on the provided integer."""
    # declare the smallest_divisor with default of None
    sm_div = None
    # exhaustively search through all of the values, starting at 2
    # --> if the number is evenly divisible, then it is not prime
    # start a for loop that will iterate over the values from '2' to 'number - 1'. Each time, the number will be divided by i.
    for i in range(2, number):
        # checks if 'number' is evenly divisible by the current value of 'i'. If it is, then 'number' is not prime and 'i' is the smallest divisor.
        if number % i == 0:
            sm_div = i
            break
    # if smallest_divisor is no longer None then the function has
    # found a non-prime number with a specific smallest_divisor
    # then return the final verdict and list of value the number can be divided: itself and sm_div
    if sm_div is not None:
        return False, [sm_div]
    # if the smallest_divisor is still None then the function has
    # found a prime number and it should return both itself and 1
    return True, [number, 1]


# define the function which taks an integer 'number' as input and returns a tuple of two values: a boolean and a list of integers
def primality_test_efficient(number: int) -> Tuple[bool, List[int]]:
    """Perform an efficient primality test on the provided integer."""
    smallest_divisor = None
    # determine first if the number is even and then confirm
    # that it does have a smallest_divisor of 2
    if number % 2 == 0:
        smallest_divisor = 2
    else:
        # if the number is not even, then iteratively perform primality test
        # use a range function that skips over the even values
        # the range function is set up like this 'range(start, stop, step)'. The 'start' value
        # is set to 3 and 'stop' is 'number. 'Step' is 2, meaning it will step by 2 and take
        # values like 3, 5, 7 into calculation.
        for i in range(3, number, 2):
            if number % i == 0:
                smallest_divisor = i
                break
    if smallest_divisor is not None:
        return False, [smallest_divisor]
    return True, [number, 1]


@cli.command()
def primality(
    number: int = typer.Option(5),
    profile: bool = typer.Option(False),
    approach: PrimalityTestingApproach = PrimalityTestingApproach.EFFICIENT,
) -> None:
    """Use iteration to perform primality testing on a number and run a profiling data collection if requested."""
    # create a console for rich text output
    console = Console()
    # create an empty primality_tuple
    primality_tuple: Tuple[bool, List[int]]
    # use the efficient primality testing algorithm
    if approach.value == PrimalityTestingApproach.EFFICIENT:
        # perform profiling on the execution of the primality test
        if profile:
            profiler.start()
            primality_tuple = primality_test_efficient(number)
            # do not perform profiling
            profiler.stop()
        else:
            primality_tuple = primality_test_efficient(number)
    # use the exhaustive primality testing algorithm
    elif approach.value == PrimalityTestingApproach.EXHAUSTIVE:
        # if requested, perform profiling test
        if profile:
            profiler.start()
            # perform primality test that will return a Tuple
            primality_tuple = primality_test_exhaustive(number)
            # do not perform profiling
            profiler.stop()
        else:
            primality_tuple = primality_test_exhaustive(number)
    # display the results of the primality test
    was_prime_found = primality_tuple[0]
    divisor_list = primality_tuple[1]
    console.print(f":smile: Attempting to determine if {number} is a prime number!")
    console.print()
    console.print(
        f":sparkles: What divisors were found? {pretty_print_list(divisor_list)}"
    )
    console.print(
        f":sparkles: Was this a prime number? {human_readable_boolean(was_prime_found)}"
    )
    # display the results of the profiling if that option was requested
    if profile:
        console.print()
        console.print(
            f":microscope: Here's profile data from performing primality testing on {number}!"
        )
        profiler.print()
