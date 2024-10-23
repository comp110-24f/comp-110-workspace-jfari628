__author__ = "730554105"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_use_case_1() -> None:
    """Testing find_and_remove_max returns max value in list"""
    assert find_and_remove_max([2, 3, 4, 7, 7]) == 7


def test_find_and_remove_max_use_case_2() -> None:
    """Testing find_and_remove_max correctly modifies list"""
    a: list[int] = [8, 3, 4, 1, 2, 10, 3]
    find_and_remove_max(a)
    assert a == [8, 3, 4, 1, 2, 3]


def test_find_and_remove_max_edge_case() -> None:
    """Testing find_and_remove_max correctly modifies unconventional list"""
    a: list[int] = [1, 1, 1, 1, 1, 1, 1, 1]
    find_and_remove_max(a)
    assert a == []
