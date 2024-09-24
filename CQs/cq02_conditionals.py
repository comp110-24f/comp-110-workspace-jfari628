"""A simple number guessing game!"""

__author__ = "730554105"


def guess_a_number() -> None:
    secret: int = 7
    guess: int = int(input("Guess a number:"))  # asks the user to input a number
    print("Your guess was " + str(guess))
    if guess == secret:  # if the guess equals the secret number do this
        print("You got it!")
    elif guess < secret:
        print(
            "Your guess was too low! The secret number is " + str(secret)
        )  # if the guess is less than the secret number do this
    elif guess > secret:
        print(
            "Your guess was too high! The secret number is " + str(secret)
        )  # if the guess is more than the secret number do this
    return None


if __name__ == "main":
    guess_a_number()
