__author__ = "730554105"

word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":

    def concat(str1: str, str2: str) -> str:
        return str1 + str2

    print(concat(word1, word2))
