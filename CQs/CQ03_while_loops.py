"""Practice with While Loops"""

__author__ = "730554105"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    while index < len(
        phrase
    ):  # checks that index is less than the length of phrase. Can't be less than or equal to, because then the condition for the while loop would always be true and the function would never exit
        if search_char == phrase[index]:
            count = count + 1
            index = index + 1
        else:
            index = index + 1

    print(count)
    return count
