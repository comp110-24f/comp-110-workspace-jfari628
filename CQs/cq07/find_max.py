__author__ = "730554105"


def find_and_remove_max(input: list[int]) -> int:
    find_idx: int = 0
    remove_idx: int = 0
    max_val: int
    if len(input) == 0:
        return -1
    else:
        max_val = input[0]
        while find_idx < len(input):
            if input[find_idx] > max_val:
                max_val = input[find_idx]
            find_idx += 1
        while remove_idx < len(input):
            if input[remove_idx] == max_val:
                input.pop(remove_idx)
            else:
                remove_idx += 1
    return max_val
