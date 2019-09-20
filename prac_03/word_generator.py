"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

def main():
    word_format = input("Please enter a word format for the random word generator:\n"
                        "\tc: Consonant\n"
                        "\tv: Vowel\n"
                        "eg. ccvcvvc\n\n").lower()
    # word_format = "ccvcvvc"
    word = ""
    valid_format = False
    while valid_format != True:
        valid_format = is_valid_format(word_format)
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    print(word)


def is_valid_format(word_format):
    for letter in word_format:
        if letter != "c" or letter != "v":
            valid_format = False
        else:
            valid_format = True
        return valid_format




main()





