import random

NUMBERS_PER_LINE = 6


def main():
    quick_picks = int(input("How many quick picks? "))
    for line in range(quick_picks):
        numbers_generated = calculate_row_numbers()
        numbers_generated.sort()
        print(numbers_generated)


def calculate_row_numbers():
    numbers = []
    for i in range(NUMBERS_PER_LINE):
        number = random.randint(1, 45)
        numbers.append(number)
    return numbers


main()

