""" Zack """


def main():
    min_password_length = 10
    password = input("Please enter a password to test: ")
    while len(password) <= min_password_length:
        password = input("Please enter a password to test: ")
    print(len(password) * ("*"))


main()
