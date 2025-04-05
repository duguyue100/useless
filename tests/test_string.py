from useless.string import reverse_reverse


def test_reverse_reverse():
    # Test with a regular string
    assert reverse_reverse("hello") == "hello"
    assert reverse_reverse("world") == "world"

    # Test with an empty string
    assert reverse_reverse("") == ""

    # Test with a single character
    assert reverse_reverse("a") == "a"

    # Test with a string containing spaces
    assert reverse_reverse("hello world") == "hello world"

    # Test with a string containing special characters
    assert reverse_reverse("!@#$%^&*()") == "!@#$%^&*()"

    # Test with a long string
    long_string = "a" * 1000
    assert reverse_reverse(long_string) == long_string
