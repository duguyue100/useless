def reverse_reverse(string: str) -> str:
    """Reverse a string and then reverse it again.

    Args:
        string: The string to reverse.

    Returns:
        str: The reversed string.
    """
    assert isinstance(string, str), "the input must be a string"

    # Reverse the string
    reversed_string = string[::-1]
    # Reverse it again
    double_reversed_string = reversed_string[::-1]

    return double_reversed_string
