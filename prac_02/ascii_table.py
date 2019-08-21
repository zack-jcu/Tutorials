# ASCII boundrys 33-127
UPPER = 127
LOWER = 33


def main():
    # character = input("Please enter a character to convert to ASCII: ")
    # ordinal = ord(character)
    # print("The ASCII code for {} is {}".format(character, ordinal))
    #
    # ascii_code = int(input("Please enter a number (between 33 & 127) to convert from ASCII: "))
    # while ascii_code not in range(LOWER, UPPER + 1):
    #     print("Invalid Number - Not in range")
    #     ascii_code = int(input("Please enter a number (between 33 & 127) to convert from ASCII: "))
    #
    # converted_character = chr(ascii_code)
    # print("The converted character from ASCII {} is {}".format(ascii_code, converted_character))

    coulomb = int(input("How many coulombs would you like to print in: "))
    ordinals_and_numbers = []
    for i in range(LOWER, UPPER + 1):
        ordinal = str(i)
        character = str(chr(i))
        appended = ordinal + " " + character
        ordinals_and_numbers.append(appended)

    for count, item in enumerate(ordinals_and_numbers):
        if count % coulomb == 0:
            print("\n")
        print(ordinals_and_numbers[count], "\t", end='')


main()
