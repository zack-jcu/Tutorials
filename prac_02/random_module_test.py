import random


def main():
    print(random.randint(5, 20))  # range between 5 & 20
    print(random.randrange(3, 10, 2))  # range between 3 & 10, in steps of 2
    print(random.uniform(2.5, 5.5))  # range between 2.5 & 5.5 (random floating point numbers)


main()
