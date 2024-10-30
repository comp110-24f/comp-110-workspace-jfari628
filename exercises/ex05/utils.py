"""Ex05 functions to be tested"""

__author__ = "730554105"


def only_evens(ints: list[int]) -> list[int]:
    idx: int = 0
    even_list: list[int] = []
    while idx < len(
        ints
    ):  # iterates over elements in list, checking if they're even/odd
        if ints[idx] % 2 == 0:
            even_list.append(ints[idx])  # adds element to new list if its even
        idx += 1
    return even_list


def sub(ints: list[int], start: int, end: int) -> list[int]:
    sub_ints: list[int] = []
    if start < 0:
        start = 0  # makes sure function starts from beginning of list
    if end > len(ints):
        end = len(ints)
    if (len(ints) == 0) or start > end:  # returns blank list
        return sub_ints
    while (
        start < end
    ):  # iterates from start to end index and adds elements to the blank list
        sub_ints.append(ints[start])
        start += 1
    return sub_ints


def add_at_index(input_list: list[int], element_add: int, add_idx: int) -> None:
    if (add_idx > len(input_list)) or (add_idx < 0):  # checks for error
        raise IndexError("Index is out of bounds for the input list")
    input_list.append(0)  # add space to the end of the list
    idx = (
        len(input_list) - 2
    )  # separate index to iterate through the input list, minus two to account for addition of space
    while idx >= add_idx:
        input_list[idx + 1] = input_list[idx]  # shifts elements to the right
        idx -= 1  # shifts all elements that are to the right of where element should be added
    input_list[add_idx] = element_add  # add the element at the correct location
