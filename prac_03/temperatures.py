"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
def main():

    MENU = """C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            input_celsius = float(input("Celsius: "))
            fahrenheit = conversion_to_fahrenheit(input_celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            input_fahrenheit = float(input("Fahrenheit: "))
            celsius = conversion_to_celsius(input_fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def conversion_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def conversion_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
