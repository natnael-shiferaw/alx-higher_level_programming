#!/usr/bin/python3

"""This Python script is designed to read
data from the standard input and calculate metrics.

It will print the following statistics after
processing every ten lines or when a keyboard
interruption (CTRL + C) is encountered:

    - The total file size accumulated up to that point.
    - The count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """A function that is used to
    print accumulated metrics.

    Args:
        size (int): represents the size of accumulated read file.
        status_codes (dict): represents the status codes.
    """

    print("File size: {}".format(size))
    for Key in sorted(status_codes):
        print("{}: {}".format(Key, status_codes[Key]))


if __name__ == "__main__":
    import sys

    Count = 0
    size = 0
    ValidCodes = ['200', '301', '400', '401', '403', '404', '405', '500']
    status_codes = {}

    try:
        for Line in sys.stdin:

            if Count == 10:
                print_stats(size, status_codes)
                Count = 1
            else:
                Count += 1

            Line = Line.split()

            try:
                size += int(Line[-1])
            except (IndexError, ValueError):
                pass

            try:

                if Line[-2] in ValidCodes:
                    if status_codes.get(Line[-2], -1) == -1:
                        status_codes[Line[-2]] = 1
                    else:
                        status_codes[Line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
