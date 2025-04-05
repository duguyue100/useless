from __future__ import annotations


def sort_numbers(array: list[int | float], reverse: bool = False) -> list[int | float]:
    """Sorts a list of numbers in ascending or descending order.

    Note that this function limits the input to a list of integers or floats.
    This might be the slowest sorting algorithm, rendered it useless.

    Args:
        array: The list of numbers to sort.
        reverse: If True, sorts in descending order. Defaults to False.

    Returns:
        list: The sorted list of numbers.
    """
    if not all(isinstance(i, (int, float)) for i in array):
        raise ValueError("All elements in the list must be integers or floats.")

    for start_idx in (
        range(len(array)) if not reverse else range(len(array) - 1, -1, -1)
    ):
        min_idx = start_idx
        for i in (
            range(start_idx, len(array)) if not reverse else range(start_idx, -1, -1)
        ):
            if array[i] < array[min_idx]:
                min_idx = i
        array[start_idx], array[min_idx] = array[min_idx], array[start_idx]

    return array
