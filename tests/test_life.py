from useless.life import is_livable


def test_is_livable():
    """Test the is_livable function."""
    assert is_livable("New York") is True
    assert is_livable("Los Angeles") is True
    assert is_livable("Chicago") is True
    assert is_livable("Houston") is True
    assert is_livable("Phoenix") is True
    assert is_livable("Philadelphia") is True
    assert is_livable("San Antonio") is True
    assert is_livable("San Diego") is True
    assert is_livable("Dallas") is True
    assert is_livable("San Jose") is True
