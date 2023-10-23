#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):

    """A Fuction that performs divsion of two lists
    element by element and output it into a new list."""

    New_List = []
    for k in range(0, list_length):
        try:
            quo = my_list_1[k] / my_list_2[k]
        except TypeError:
            print("wrong type")
            quo = 0
        except ZeroDivisionError:
            print("division by 0")
            quo = 0
        except IndexError:
            print("out of range")
            quo = 0
        finally:
            New_List.append(quo)
    return New_List
