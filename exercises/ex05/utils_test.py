"""Ex05 unit tests"""

__author__ = "730554105"


from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_edge_case() -> None:
    """Edge case: Empty list"""
    assert only_evens([]) == []


def test_only_evens_use_case_1() -> None:
    """Use case: Mix of even and odd numbers"""
    assert only_evens([122, 15, 2467, 346]) == [122, 346]


def test_only_evens_use_case_2() -> None:
    """Use case: All even numbers"""
    assert only_evens([2, 4, 6, 8]) == [2, 4, 6, 8]


def test_sub_edge_case() -> None:
    """Edge case: Start index is greater than end index"""
    assert sub([10, 20, 30, 40], 3, 1) == []


def test_sub_use_case_1() -> None:
    """Use case: Subset within valid range"""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_sub_use_case_2() -> None:
    """Use case: Empty list"""
    assert sub([], 1, 3) == []


def test_add_at_index_edge_case() -> None:
    """Edge case: Add element at an out-of-bounds index"""
    list_1 = [7, 8, 10]
    with pytest.raises(IndexError):
        add_at_index(list_1, 2, 9)


def test_add_at_index_use_case_1() -> None:
    """Use case: Adding element in the middle of the list"""
    list_1 = [1, 2, 3, 5]
    add_at_index(list_1, 4, 3)
    assert list_1 == [1, 2, 3, 4, 5]


def test_add_at_index_use_case_2() -> None:
    """Use case: Try adding to an empty list (should raise IndexError)"""
    list_2 = []
    with pytest.raises(IndexError):
        add_at_index(list_2, 0, 1)
