from useless.algo import sort


def test_sort():
    """Test the sort function."""
    assert sort([3, 1, 4, 1, 5, 9]) == [1, 1, 3, 4, 5, 9]
    assert sort([3.2, 1.1, 4.5, 1.0, 5.8]) == [1.0, 1.1, 3.2, 4.5, 5.8]
    assert sort([3, -1, -4, -1, -5]) == [-5, -4, -1, -1, 3]
    assert sort([3]) == [3]
    assert sort([]) == []
    assert sort([3, -1, -4, -1, -5], reverse=True) == [3, -1, -1, -4, -5]
    assert sort([3.2], reverse=True) == [3.2]
    assert sort([3], reverse=True) == [3]
    assert sort([], reverse=True) == []
