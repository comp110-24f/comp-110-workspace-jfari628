__author__ = "730554105"


def get_coords(xs: str, ys: str) -> None:
    index1: int = 0
    while index1 < len(xs):  # iterate over every char in xs
        index2: int = 0
        while index2 < len(ys):  # iterate over every char in ys
            print(f"({xs[index1]},{ys[index2]})")
            index2 = index2 + 1
        index1 = index1 + 1
