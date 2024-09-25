"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730554105"


def input_word() -> str:  # will ask the user to enter a 5 character word
    word_guess: str = input("Enter a 5-character word:")
    if len(word_guess) == 5:
        print(word_guess)
    else:
        print("Error: Word must contain 5 characters.")
        exit()  # exits the function before returning word_guess
    return word_guess


def input_letter() -> str:  # will ask the user to enter a letter
    letter_guess: str = input("Enter a single character:")
    if len(letter_guess) == 1:
        print(letter_guess)
    else:
        print("Error: Character must be a single character.")
        exit()  # exits the function before returning letter_guess
    return letter_guess


def contains_char(
    word: str, letter: str
) -> (
    None
):  # check if the input character matches any of the characters in the input word
    # word = str(input_word)
    # letter = str(letter_guess)
    matches: int = (
        0  # initialized at 0 because thats how many matches there should be before
        # anything runs
    )
    print("Searching for " + letter + " in " + word)
    if (
        letter == word[0]
    ):  # need individual if statements so every index is checked and the code doesn't
        # stop if the elif/else condition is true
        print(letter + " found at index 0")
        matches = matches + 1

    if letter == word[1]:
        print(letter + " found at index 1")
        matches = matches + 1
    if letter == word[2]:
        print(letter + " found at index 2")
        matches = matches + 1
    if letter == word[3]:
        print(letter + " found at index 3")
        matches = matches + 1
    if letter == word[4]:
        print(letter + " found at index 4")
        matches = matches + 1
    if matches == 0:
        print("No instances of " + letter + " found in " + word)
    elif matches == 1:
        print("1 instance of " + letter + " found in " + word)
    elif matches >= 2:
        print(str(matches) + " instances of " + letter + " found in " + word)


def main() -> (
    None
):  # putting it all together, handles the calls for each individual function
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
