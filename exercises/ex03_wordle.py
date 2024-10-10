"""A fun, word-guessing game!"""

__author__ = "730554105"


def input_guess(
    secret_word_len: int,
) -> str:  # prompts the user to enter a word that's the same length as secret word
    """Prompts the user for a word guess"""
    word_guess: str = input("Enter a " + str(secret_word_len) + " character word:")
    while (
        len(word_guess) != secret_word_len
    ):  # reprompts user to enter correct lenght word
        word_guess = input(
            f"That wasn't {secret_word_len} chars! Try again:"
        )  # updates word_guess so loop isn't infinite

    return word_guess


def contains_char(word: str, character: str) -> bool:
    """Checking word for any instances of character"""
    assert len(character) == 1
    index: int = 0
    matches: int = 0
    while index < len(
        word
    ):  # iterates through every index of word to check for character
        if character == word[index]:
            matches = matches + 1
        index = index + 1
    return (
        matches > 0
    )  # Anything above 0 should return True because that means there's a match


def emojified(user_guess: str, secret_word: str) -> str:
    """Assigning emojis to the "correctness" of characters in word"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(user_guess) == len(secret_word)
    index: int = 0
    result: str = ""  # empty string used to build emoji string
    while index < len(user_guess):
        if user_guess[index] == secret_word[index]:
            result += f"{GREEN_BOX}"  # += operator adds to the string and includes everything that came before it
        elif contains_char(
            word=secret_word, character=user_guess[index]
        ):  # uses contains_char to look for matches. True = Yellow Box
            result += f"{YELLOW_BOX}"
        else:
            result += f"{WHITE_BOX}"
        index = index + 1
    return result


def main(secret: str) -> None:
    """Counts the number of turns and determines if user won"""
    turn: int = 1  # keeps track of the number of turns
    while turn <= 6:
        user_guess: str = input_guess(
            secret_word_len=len(secret)
        )  # keeps track of user_guess and reprompts user to guess if previous argument for user_guess != secret
        print(f"=== Turn {turn}/6 ===")
        print(emojified(user_guess=user_guess, secret_word=secret))
        if (
            user_guess == secret
        ):  # checks if user_guess == secret, otherwise reprompts user to guess again
            print(f"You won in {turn}/6 turns!")
            return None
        turn += 1
    if turn > 6:
        print("X/6 - Sorry, try again tomorrow!")
        return None


if __name__ == "__main__":
    main(secret="codes")
