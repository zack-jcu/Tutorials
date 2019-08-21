def main():
    user_name = (input("please enter your name: "))
    write_file = open("name.txt", "w")
    print(user_name, file=write_file)
    write_file.close()

    read_file = open("name.txt", "r")
    for each_line in read_file:
        print(each_line.rstrip())
    read_file.close()

    file_list = []
    read_file = open("numbers.txt", "r")
    for each_line in read_file:
        print(each_line)
        file_list.append(int(each_line.rstrip()))
    read_file.close()
    print(file_list)
    total = 0
    for each_number in file_list:
        total += each_number
    print("Total: ", total)


main()
