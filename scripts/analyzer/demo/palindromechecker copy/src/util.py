"""Generate human_readable boolean expression."""


# implement the def get_human_readable_boolean(answer: bool) -> str function
def human_readable_boolean(answer: bool) -> str:
    """Express a bool value in a human-readable fashion."""
    # condition logic for answer
    if answer:
        return "Yes, it is!"
    return "No, it is not!"
