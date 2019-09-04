import statistics

NUMBER_PROMPTS = 5


def main():
    numbers = []
    prompt_count = 0
    while prompt_count != 5:
        number = input("Please enter a number: ")
        numbers.append(int(number))
        prompt_count += 1
    print("length of list = {}".format(len(numbers)))
    print("First number: {}".format(numbers[0]))
    print("Last number: {}".format(numbers[-1]))
    print("reversed: {}".format(numbers[::-1]))
    print("Smallest: {}".format(min(numbers)))
    print("Largest: {}".format(max(numbers)))
    print("Sum: {}".format(sum(numbers)))
    print("Average: {}".format(sum(numbers) / NUMBER_PROMPTS))


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Please enter your username: ")
if username in usernames:
    print("Access Granted")
else:
    print("Access Denied")

main()
