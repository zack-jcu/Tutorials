"""
Create a file called loops.py and add this for loop that displays all of the odd numbers between
1 and 20 with a space between each one.
"""

for i in range(1, 21, 2):
    print(i, end=" ")
print()

# count in 10s from 0 to 100

for i in range(0, 110, 10):
    print(i, end=" ")
print()

# count down from 20 to 1

for i in range(20, 0, -1):
    print(i, end=" ")
print()

# print n stars. Ask the user for a number, then print that many stars (*), all on one line

number_of_stars = int(input("Number of Stars: "))
print(number_of_stars * "*")

# As above but in a loop
number_of_stars = int(input("Number of Stars: "))
for i in range(number_of_stars):
    print("*", end=" ")
print()

# print n lines of increasing stars. Using the same number as above print lines of increasing stars, starting at 1. E.g.
# if 4 was the number entered, your single loop should print
number_of_stars = int(input("Number of Stars: "))
for i in range(1, number_of_stars + 1):
    print("*" * i)
print()
