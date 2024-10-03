"""Practice with Lists"""

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

# Add to a list
my_numbers.append(1.5)
my_numbers.append(2.3)

print(my_numbers)

# Create an already populated list
game_points: list[int] = [102, 86, 94]

# Subscription Notation/Indexing
print(game_points[2])

# Modifying Elements
game_points[1] = 72
game_points[2] = 72


# Getting the length
print(len(game_points))
y: int = len(game_points)  # Storing the len as a variable
print(y)

# Removing items from lists
game_points.pop(1)


def display(Input: list[int] = [0, 1, 2, 3, 4, 5]) -> None:
    index: int = 0
    while index < len(Input):
        print(Input[index])
        index = index + 1


display()
