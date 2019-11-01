import string
import random

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SPECIAL = string.punctuation

# print(LOWER)
# print(UPPER)
# print(DIGITS)
# print(SPECIAL)

print("*** Password Generator ***\n")
length = int(input("Please enter the desired password length: "))
upper = int(input("How many upper case characters: "))
digits = int(input("How many numbers: "))
special = int(input("How many special characters: "))
mixed = upper + digits + special

while mixed > length:
    print("Oops, you have more requirements than characters")
    length = int(input("Please enter the desired password length: "))
    upper = int(input("How many upper case characters: "))
    digits = int(input("How many numbers: "))
    special = int(input("How many special characters: "))
    mixed = upper + digits + special

lower = length - mixed
random_upper = random.sample(UPPER, upper)
random_digits = random.sample(DIGITS, digits)
random_special = random.sample(SPECIAL, special)
random_lower = random.sample(LOWER, lower)

joined = random_upper + random_digits + random_special + random_lower
print(joined)
random.shuffle(joined)
print(joined)
# print(len(joined))
print("Password: ", end='')
for letter in joined:
    print(letter, end='')
