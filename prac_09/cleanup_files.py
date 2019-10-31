"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os
import re


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    os.chdir('Lyrics/Sunday')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

    for filename in filenames:

        if os.path.isdir(filename):
            continue

        underscore = re.sub(r"(?<=\w)([A-Z])", r"_\1", filename)
        fixed_name = underscore.replace(" ", "_").replace(".TXT", ".txt").replace(".T_X_T", ".txt")
        # print("{}, {}".format(filename, fixed_name))

        full_name = os.path.join(directory_name, filename)
        new_name = os.path.join(directory_name, fixed_name)
        print("{}, {}".format(full_name, new_name))
        os.rename(full_name, new_name)


main()
