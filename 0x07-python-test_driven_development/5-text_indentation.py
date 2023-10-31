#!/usr/bin/python3
"""A PYTHON FILE THAT DEFINES A FUNCTION
THAT IS USED FOR INDENTATION OF TEXT."""


def text_indentation(text):
    """A FUNCTION USED TO PRINT TEXT WITH 2 NEW LINES AFTER '.' , '?', ':'

    Args:
        text (string): TEXT TO BE PRINTED.
    Raises:
        TypeError: IF TEXT IS ANYTHING OTHER THAN STRING.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    H = 0

    while H < len(text) and text[H] == ' ':
        H += 1

    while H < len(text):
        print(text[H], end="")

        if text[H] == "\n" or text[H] in ".?:":
            if text[H] in ".?:":
                print("\n")
            H += 1
            while H < len(text) and text[H] == ' ':
                H += 1
            continue

        H += 1
