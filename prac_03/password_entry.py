""" Zack """


def main():
    min_password_length = 10
    password = get_password(min_password_length)
    print(len(password) * "*")


def get_password(min_password_length):
    password = input("Please enter a password to test: ")
    while len(password) <= min_password_length:
        password = input("Please enter a password to test: ")
    return password


main()
