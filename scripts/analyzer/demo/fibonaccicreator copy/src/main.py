"""Perform an experiment to study efficiency of Fibonacci algorithms."""

import os
import time
from resource import RUSAGE_SELF
from resource import getrusage

import psutil  # type: ignore
import typer
from pyinstrument import Profiler  # type: ignore
from rich.console import Console

from fibonaccicreator import fibonacci

# Note that certain versions of Windows may not be able to
# correctly use these modules in the resource package. If you are
# running Windows and cannot get this to work, please talk with the
# course instructor about an alternative arrangement. With that said,
# this import and the use of its modules in this program should normally
# work correctly on both the MacOS and Linux operating systems.


FIBONACCI_FUNCTION_BASE = "fibonacci"
UNDERSCORE = "_"


# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a Profiler object to support timing program code segments
profiler = Profiler(interval=0.01 * 10)

# Certain versions of MacOS do not support the calculation
# of human-readable memory in bytes in a standard fashion. As such,
# you may need to re-write one or more lines of source code in this
# function if you notice that the program is reporting that it is
# using either kilo-bytes (KB) or giga-bytes (GB) of memory. In
# particular, using only a few KB of memory would probably be too little
# and using many GB of memory would probably be too much!


def format_bytes(size):
    """Format an output value in bytes in a human-readable fashion."""
    # Reference:
    # https://stackoverflow.com/questions/12523586/python-format-size-application-converting-b-to-kb-mb-gb-tb/37423778
    power = 2**16
    n = 0
    power_labels = {0: "", 1: "kilo", 2: "mega", 3: "giga", 4: "tera"}
    while size > power:
        size /= power
        n += 1
    return str(size) + " " + power_labels[n] + "bytes"


@cli.command()
def fibonaccicreator(
    approach: str = typer.Option(...),
    number: int = typer.Option(...),
    display: bool = typer.Option(False, "--display"),
    pyinstrument: bool = typer.Option(False, "--pyinstrument"),
):
    """Create the list of Fibonacci values in a specified approach."""
    # make sure that you understand all the steps in this function
    # create a console for rich text output
    console = Console()
    # display the debugging output for the program's command-line arguments
    console.print("")
    console.print(f":luggage: Awesome, the chosen type of approach is the {approach}!")
    console.print("")
    console.print(
        f":abacus: The program will compute up to the {number}th Fibonacci number!"
    )
    console.print("")
    # construct the full name of the function to call "fibonacci_(approach name)"
    function = FIBONACCI_FUNCTION_BASE + UNDERSCORE + approach
    # construct the requested function from the compute module
    # Reference: https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
    # getattr: get attribute of a class (if a Person has a name, I can do 'getattr(person,attr_name) given that person = Person() and attr_name = 'name'
    function_to_call = getattr(fibonacci, function)
    # call the constructed function and capture the result
    profiler.start()
    start = time.time()
    fibonacci_result = function_to_call(number)
    end = time.time()
    profiler.stop()
    # display debugging information with the function's output
    if display:
        console.print(f":sparkles: This is the output from the {approach} function:")
        console.print()
        # display the output from the computation
        console.print(str(fibonacci_result))
        console.print()
    # display a final message and some extra spacing, asking a question
    # about the efficiency of the approach to computing the number sequence
    console.print(
        "🤷 So, was this an efficient approach for storing the Fibonacci sequence?"
    )
    console.print("")
    process = psutil.Process(os.getpid())
    # display the estimated overall memory use as reported by the operating system
    # Reference:
    # https://stackoverflow.com/questions/938733/total-memory-used-by-python-process
    console.print("Estimated overall memory according to the operating system:")
    console.print("   " + format_bytes(process.memory_info().vms))
    console.print("")
    # display the estimated peak memory use as reported by the operating system
    # Reference:
    # https://pythonspeed.com/articles/estimating-memory-usage/
    console.print("Estimated peak memory according to the operating system:")
    console.print("   " + format_bytes(getrusage(RUSAGE_SELF).ru_maxrss * 1024))
    console.print()
    # display a simplified execution time
    # Reference:
    # https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
    console.print("Estimated execution time according to the simple timer:")
    console.print(f"    {(end - start):.2f} seconds")
    # display the execution time recorded by the pyinstrument package
    # Reference:
    # https://pyinstrument.readthedocs.io/en/latest/guide.html#profile-a-specific-chunk-of-code
    if pyinstrument:
        console.print()
        console.print(
            ":bookmark: Estimated execution time according to pyinstrument displayed in your browser!"
        )
        profiler.open_in_browser()
