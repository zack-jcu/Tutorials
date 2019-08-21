"""
Menu-driven number sequence generator:
A school teacher requires a small program that would allow primary school students to learn about various number
sequences. The teacher is interested in a simple menu-driven program that has the following choices
(where x and y are inputs the user enters once at the start of the program):

Show the even numbers from x to y
Show the odd numbers from x to y
Show the squares from x to y
Exit the program
"""

print("*** Number Sequence Teacher ***")
start = int(input("please enter the start number: "))
finish = int(input("please enter the finish number: "))
print("(E)ven\n"
      "(O)dd\n"
      "(S)quares\n"
      "(Q)uit\n")
user_choice = input("Selection: ").upper()
while user_choice != "Q":
    if user_choice == "E":
        if (start % 2) != 0:
            start = start + 1
        for i in range(start, finish, 2):
            print(i, end=" ")
    elif user_choice == "O":
        if (start % 2) == 0:
            start = start + 1
        for i in range(start, finish, 2):
            print(i, end=" ")
    elif user_choice == "S":
        for i in range(start, finish):
            print(i * i, end=" ")
    else:
        print("Invalid Selection")
    print("\n")
    print("(E)ven\n"
          "(O)dd\n"
          "(S)quares\n"
          "(Q)uit\n")
    user_choice = input("Selection: ").upper()
print("Finished")
