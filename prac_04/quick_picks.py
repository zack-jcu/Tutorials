import random

NUMBERS_PER_LINE = 6


def main():
    quick_picks = int(input("How many quick picks? "))
    for line in range(quick_picks):
        numbers_generated = calculate_number_of_rows()
        numbers_generated.sort()
        print(numbers_generated)


def calculate_number_of_rows():
    numbers = []
    for i in range(NUMBERS_PER_LINE):
        number = random.randint(1, 45)
        numbers.append(number)
    return numbers


main()

