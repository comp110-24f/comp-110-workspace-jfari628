"""A program to help plan a tea party"""

__author__: str = "730554105"


def main_planner(guests: int) -> None:
    """Function that will call the tea_bags, treats, and cost functions, and then print their outputs"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(
                tea_count=tea_bags(people=guests), treat_count=treats(people=guests)
            )  # call the cost function, all of the cost function's parameters are based on the return values of tea_bags and treats.
        )
    )
    return None


def tea_bags(people: int) -> int:  # Defining the tea_bags function
    """Calculate the number of tea bags based on the number of people"""
    return (
        people * 2
    )  # Need to multiply the number of people times 2 because everyone is drinking 2 teas


def treats(people: int) -> int:
    """Calculate the number of treats based on the number of teas guests are expecting to drink"""
    return int(tea_bags(people=people) * 1.5)


# Account for relationship between number of teas drank and number of treats to be eaten
# Need to call the tea_bags function within the return statement of the treats function and then multiply by 1.5
# Use a keyword argument to equate people and people.


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the cost of the tea bags plus the cost of the treats"""
    return (tea_count * 0.50) + (
        treat_count * 0.75
    )  # number of teas * 0.50 + number of treats * 0.75 = total cost
    # these parameters don't rely on the return value of any of the other functions!


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
