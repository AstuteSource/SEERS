"""Determine whether or not an input string is a palindrome."""

# Reference:
# https://en.wikipedia.org/wiki/Palindrome


def to_char(word: str) -> str:
    """Convert string to character."""
    word = word.lower()
    letters = ""
    for char in word:
        if char in "abcdefghijklmnopqrstuvwxyz":
            letters = letters + char
    return letters


# implement def is_palindrome(word: str) -> bool:
def is_palindrome(word: str) -> bool:
    """Check palindrome."""
    if len(word) <= 1:
        return True
    return word[0] == word[-1] and is_palindrome(word[1:-1])


# implement def is_palindrome_recursive(word: str) -> bool:
def is_palindrome_recursive(word: str) -> bool:
    """Check palindrome with recursive approach."""
    return is_palindrome(to_char(word))


# implement def is_palindrome_reverse(word: str) -> bool:
def is_palindrome_reverse(word: str) -> bool:
    """Check palindrome with reverse approach."""
    char_list = list(word)
    char_list.reverse()
    return char_list == list(word)
