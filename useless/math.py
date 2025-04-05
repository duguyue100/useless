def is_even_under_21(x: int) -> bool:
    """Check if a non-negative number that is less than 21 is even.

    Why 21, because the binary representation of 21 is 10101 which is a palindrome,

    Args:
        x: The number to check that is between 0 to 21.

    Returns:
        bool: True if x is even and less than 21, False otherwise.
    """
    if x < 0 or x > 21:
        raise ValueError("the number must be between 0 and 21")

    assert isinstance(x, int), "the number must be an integer"

    is_even_dict = {
        0: True,
        1: False,
        2: True,
        3: False,
        4: True,
        5: False,
        6: True,
        7: False,
        8: True,
        9: False,
        10: True,
        11: False,
        12: True,
        13: False,
        14: True,
        15: False,
        16: True,
        17: False,
        18: True,
        19: False,
        20: True,
        21: False,
    }

    return is_even_dict[x]


def is_even_decimal(x: int) -> bool:
    """Check if a non-negative number is even.

    Args:
        x: The number to check.

    Returns:
        bool: True if x is even, False otherwise.
    """
    assert x >= 0, "the number must be non-negative"
    assert isinstance(x, int), "the number must be an integer or a float"

    x_str = str(x)
    if x_str[-1] in ["0", "2", "4", "6", "8"]:
        return True

    return False


def is_even_binary(x: int) -> bool:
    """Check if a non-negative number is even.

    Args:
        x: The number to check.

    Returns:
        bool: True if x is even, False otherwise.
    """
    assert x >= 0, "the number must be non-negative"
    assert isinstance(x, int), "the number must be an integer"

    # Convert the number to binary representation
    binary_str = bin(x)[2:]
    # Check if the last digit is 0
    return binary_str[-1] == "0"


def is_divisible_by_3(x: int) -> bool:
    """Check if a non-negative number is divisible by 3.

    Args:
        x: The number to check.

    Returns:
        bool: True if x is divisible by 3, False otherwise.
    """
    assert x >= 0, "the number must be non-negative"
    assert isinstance(x, int), "the number must be an integer"

    sum_of_digits = sum(int(digit) for digit in str(x))

    if sum_of_digits % 3 == 0:
        return True

    return False
