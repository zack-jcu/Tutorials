import os


def main():
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        if os.path.isdir(extension):
            pass
        else:
            os.mkdir(extension)
        print("{}/{}".format(extension, filename))
        os.rename(filename, "{}/{}".format(extension, filename))


main()

