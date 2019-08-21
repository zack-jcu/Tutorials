"""
get name
display menu
get user_choice
while user_choice != quit option
    if user_choice == first option
        do first task
    else if user_choice == <second option>
        do second task
    ...
    else if user_choice == <n-th option>
        do n-th task
    else
        display invalid input error message
    display menu
    get user_choice
do final thing, if needed
"""

user_name = input("Enter name: ")
print("(H)ello\n"
      "(G)oodbye\n"
      "(Q)uit\n")
user_choice = input("Selection: ").upper()
while user_choice != "Q":
    if user_choice == "H":
        print("Hello")
    elif user_choice == "G":
        print("Goodbye")
    else:
        print("Invalid Selection")
    print("(H)ello\n"
          "(G)oodbye\n"
          "(Q)uit\n")
    user_choice = input("Selection: ").upper()
print("Finished")

