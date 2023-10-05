#!/usr/bin/python3

"""This program is used to print all the
names defined by the hidden_4 module. """

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for n in names:
        if n[:2] != "__":
            print(n)
