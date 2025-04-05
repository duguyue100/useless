import pytest

from useless.math import is_even_decimal
from useless.math import is_even_under_21


def test_is_even_under_21():
    for i in range(-1, 73):
        if i < 0 or i > 21:
            with pytest.raises(ValueError):
                is_even_under_21(i)
        else:
            assert is_even_under_21(i) == (i % 2 == 0)


def test_is_even_decimal():
    for i in range(-1, 73):
        if i < 0:
            with pytest.raises(AssertionError):
                is_even_decimal(i)
        else:
            assert is_even_decimal(i) == (i % 2 == 0)
