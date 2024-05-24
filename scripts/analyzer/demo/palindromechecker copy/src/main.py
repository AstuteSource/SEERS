"""Perform testing Palindrome on string input."""
# provide a descriptive docstring for the module

from enum import Enum

# import all of the required packages and modules
import typer
from rich.console import Console

from src import palindrome
from src import util

# create the command-line interface object with typer
cli = typer.Typer()

# define a PalindromeCheckingApproach enumeration with these options:
# --> "RECURSIVE": use the recursive approach described on page 129
# --> "REVERSE": use the recursive approach described on page 164


class PalindromeApproach(str, Enum):
    """Define the name for the approach for performing Palindrome testing."""

    RECURSIVE = "recursive"
    REVERSE = "reverse"

    def __str__(self):
        """Create string function."""
        return self.value if self is not None else ""


# When you are setting the default values of the --approach variable
# you may need to consider how to extract a value from PalindromeCheckingApproach
# Please refer to this GitHub issue tracker discussion for more details:
# https://github.com/tiangolo/typer/issues/290


@cli.command()
def palindrome_check(
    word: str = typer.Option(...),
    approach: PalindromeApproach = PalindromeApproach.RECURSIVE,
) -> None:
    """Test an input string to be a Palindrome."""
    # create a console for rich text output
    console = Console()

    # Recursive: execution with Recursive approach
    if approach == PalindromeApproach.RECURSIVE:
        result = palindrome.is_palindrome_recursive(word)
    # Reverse: execute with Reverse approach
    elif approach == PalindromeApproach.REVERSE:
        result = palindrome.is_palindrome_reverse(word)

    console.print(f"✨ Awesome, using the {approach} approach for palindrome checking!")
    console.print()
    console.print(f"🔖 Going to check to see if the word {word} is a palindrome!")
    console.print()
    console.print(f"😆 Is this word a palindrome? {util.human_readable_boolean(result)}")


# implement a command-line interface using typer that produces
# output like those examples included in the remainder of this file

# poetry run palindromechecker --help

# Usage: palindromechecker [OPTIONS]
#
#   Use a method to determine if an input string is a palindrome or not.
#
# Options:
#   --word TEXT                     [required]
#   --approach [recursive|reverse]  [default: reverse]
#   --install-completion            Install completion for the current
#                                   shell.
#
#   --show-completion               Show completion for the current shell,
#                                   to copy it or customize the
#                                   installation.
#
#   --help                          Show this message and exit.

# poetry run palindromechecker --word civic --approach recursive

# ✨ Awesome, using the recursive approach for palindrome checking!

# 🔖 Going to check to see if the word "civic" is a palindrome!

# 😆 Is this word a palindrome? Yes, it is!
