"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = input("Please enter a word format for the random word generator:\n"
                    "\tc: Consonant\n"
                    "\tv: Vowel\n"
                    "eg. ccvcvvc\n\n").lower()
# word_format = "ccvcvvc"
word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)
print(word)
read_file = open('words_alpha.txt', 'r')
# if word in read_file:
#     print("This is a dictionary word")
# else:
#     print("this is not a dictionary word")
for each_line in read_file:
    if each_line.rstrip() == word:
        print("\n*** Match ***\n")

read_file.close()
