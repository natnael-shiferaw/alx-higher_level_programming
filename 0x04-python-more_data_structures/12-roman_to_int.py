#!/usr/bin/python3


def to_subtract(list_num):
    To_sub = 0
    Max_list = max(list_num)

    for i in list_num:
        if Max_list > i:
            To_sub += i

    return (Max_list - To_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0
    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_num.keys())

    Num = 0
    last_rom = 0
    list_num = [0]

    for char in roman_string:
        for r_num in list_keys:
            if r_num == char:
                if rom_num.get(char) <= last_rom:
                    Num += to_subtract(list_num)
                    list_num = [rom_num.get(char)
                else:
                    list_num.append(rom_num.get(char))
                    last_rom = rom_num.get(char)

    Num += to_subtract(list_num)
    return (Num)
