#!/usr/bin/python3

"""This program is used to print the
number of arguments and list of arguments."""

if __name__ == "__main__":
    import sys

    Count = len(sys.argv) - 1
    if Count == 0:
        print("0 arguments.")
    elif Count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(Count))
    for n in range(Count):
        print("{}: {}".format(n + 1, sys.argv[n + 1]))
