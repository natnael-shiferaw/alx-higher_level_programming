#!/usr/bin/python3

"""This program is used to print the addition of all the arguments. """
if __name__ == "__main__":
    import sys

    total = 0
    for n in range(len(sys.argv) - 1):
        total += int(sys.argv[n + 1])
        print("{}".format(total))
