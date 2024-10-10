"""Reproducing list utility functions"""

__author__ = "730554105"


def all(input: list[int], number: int) -> bool:
    """Checks to see if the list is made up of ONLY number"""
    matches: int = 0
    index: int = 0
    while index < len(input) and len(input) > 0:  # makes sure the list isn't empty
        if number == input[index]:
            matches += 1  # keeps track of number of matches. If the output of the function all is True, that means matches should match the length of the list input
        index += 1
    return (
        matches == len(input) and len(input) > 0
    )  # will return True on if matches == list length AND list length isn't zero


def max(input: list[int]) -> int:
    """Returns the biggest number in the list"""
    biggest_num: int = input[0]  # starts as just the first element in the list
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    for element in input:
        if element > biggest_num:
            biggest_num = element  # stores a the new, bigger, number as the biggest_num
    return biggest_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if every element at every index in list1 is equal to every element at every index in list2"""
    index: int = 0
    matches: int = 0
    if list1 == [] and list2 == []:  # if both lists are empty, they are equal
        return True
    if len(list1) == len(
        list2
    ):  # check if the two lists are the same length and then check for matches
        while index < len(list1):
            if list1[index] == list2[index]:
                matches += 1
            index += 1  # this should be out of the if statement otherwise the while loop will never exit
        return matches == len(list1)
    return False  # return False if lengths of lists don't match


def extend(a: list[int], b: list[int]) -> None:
    """Adds elements of 2nd list onto the end of the 1st list"""
    index: int = 0
    while index < len(b):  # use a while loop because I want to iterate through indexes
        a.append(b[index])  # will add the element of b at [index] onto a
        index += 1
    print(a)
