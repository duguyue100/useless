import pytest

from useless.math import is_divisible_by_3
from useless.math import is_divisible_by_7
from useless.math import is_even_binary
from useless.math import is_even_decimal
from useless.math import is_even_upto_21
from useless.math import is_odd_binary
from useless.math import is_odd_decimal
from useless.math import is_odd_under_21


HOLY_NUMBER_MIN = -1
HOLY_NUMBER_MAX = 73


def test_is_even_upto_21():
    for i in range(HOLY_NUMBER_MIN, HOLY_NUMBER_MAX):
        if i < 0 or i > 21:
            with pytest.raises(ValueError):
                is_even_upto_21(i)
        else:
            assert is_even_upto_21(i) == (i % 2 == 0)


def test_is_odd_under_21():
    for i in range(HOLY_NUMBER_MIN, HOLY_NUMBER_MAX):
        if i < 0 or i > 21:
            with pytest.raises(ValueError):
                is_odd_under_21(i)
        else:
            assert is_odd_under_21(i) == (i % 2 != 0)


def test_is_even_decimal():
    for i in range(HOLY_NUMBER_MIN, HOLY_NUMBER_MAX):
        if i < 0:
            with pytest.raises(AssertionError):
                is_even_decimal(i)
        else:
            assert is_even_decimal(i) == (i % 2 == 0)


def test_is_odd_decimal():
    for i in range(HOLY_NUMBER_MIN, HOLY_NUMBER_MAX):
        if i < 0:
            with pytest.raises(AssertionError):
                is_odd_decimal(i)
        else:
            assert is_odd_decimal(i) == (i % 2 != 0)


def test_is_even_binary():
    for i in range(HOLY_NUMBER_MIN, HOLY_NUMBER_MAX):
        if i < 0:
            with pytest.raises(AssertionError):
                is_even_binary(i)
        else:
            assert is_even_binary(i) == (i % 2 == 0)


def test_is_odd_binary():
    for i in range(HOLY_NUMBER_MIN, HOLY_NUMBER_MAX):
        if i < 0:
            with pytest.raises(AssertionError):
                is_odd_binary(i)
        else:
            assert is_odd_binary(i) == (i % 2 != 0)


def test_is_divisible_by_3():
    for i in range(HOLY_NUMBER_MIN, HOLY_NUMBER_MAX):
        if i < 0:
            with pytest.raises(AssertionError):
                is_divisible_by_3(i)
        else:
            assert is_divisible_by_3(i) == (i % 3 == 0)


def test_is_divisible_by_7():
    for i in range(HOLY_NUMBER_MIN, HOLY_NUMBER_MAX):
        if i < 0:
            with pytest.raises(AssertionError):
                is_divisible_by_7(i)
        else:
            assert is_divisible_by_7(i) == (i % 7 == 0)
