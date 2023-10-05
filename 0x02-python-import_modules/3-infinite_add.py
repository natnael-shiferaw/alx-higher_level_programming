#!/usr/bin/python3

"""This program is used to print the addition of all the arguments. """

if __name__ == "__main__":
    import sys
    res = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            res += int(arg)
    print(res)
