from prac_06.Guitar import Guitar


def main():
    my_guitars = []
    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        my_guitars.append(new_guitar)
        print("{} ({}) : ${} added.".format(name, year, cost))
        name = input("Name: ")

    # my_guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # my_guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars:")
    for i, guitar in enumerate(my_guitars, 1):
        is_vintage = ""
        if guitar.is_vintage():
            is_vintage = "(Vintage)"
        print("Guitar {}: {} ({}), worth ${} {}".format(i, guitar.name, guitar.year, guitar.cost, is_vintage))


main()
