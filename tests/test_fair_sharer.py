from fairsharer.fair_sharer import fair_sharer


def test_examples():
    assert fair_sharer([0, 1000, 800, 0], 1) == [100, 800, 900, 0]
    assert fair_sharer([0, 1000, 800, 0], 2) == [100, 890, 720, 90]


def test_zero_iterations():
    assert fair_sharer([5, 1, 2], 0) == [5, 1, 2]


def test_ring_neighbors():
    # max=10 at index 0 -> gives 1 to left (index 2) and 1 to right (index 1)
    assert fair_sharer([10, 0, 0], 1) == [8, 1, 1]


def test_result_is_ints():
    result = fair_sharer([0, 1000, 800, 0], 2)
    assert all(isinstance(x, int) for x in result)
