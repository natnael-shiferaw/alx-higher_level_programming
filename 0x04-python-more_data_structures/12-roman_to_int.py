#!/usr/bin/python3


def roman_to_int(roman_string):

    if not isinstance(roman_string, str):
        return 0
    if roman_string is None:
        return 0

    TOKEN = roman_string.upper()
    NUMERALS = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500}
    END = len(TOKEN) - 1
    RESULT = 0

    for idx, char in enumerate(TOKEN):
        if idx < END and NUMERALS[char] < NUMERALS[TOKEN[idx + 1]]:
            RESULT -= NUMERALS[char]
        else:
            RESULT += NUMERALS[char]

    return RESULT
