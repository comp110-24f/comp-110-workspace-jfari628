"""Practicing conditionals."""


def check_first_letter(word: str, letter: str) -> str:
    """Checks if letter is first character of word"""
    if letter == word[0]:
        return "match!"
    else:
        return "no match!"
