import os

folder_to_extensions = {}


def main():
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]
        if extension not in folder_to_extensions:
            category = input("What category would you like to sort {} files into? ".format(extension))
            folder_to_extensions[extension] = category

            if not os.path.isdir(category):
                os.mkdir(category)

            # if os.path.isdir(category):  # is Try/Except better??
            #     pass
            # else:
            #     os.mkdir(category)
        os.rename(filename, "{}/{}".format(folder_to_extensions[extension], filename))  # Stolen from solution, Better


main()
