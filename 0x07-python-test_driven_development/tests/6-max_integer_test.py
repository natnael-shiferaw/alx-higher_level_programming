#!/usr/bin/python3
"""THIS PYTHON FILE USES THE Unittest MODULE FOR max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class MAX_INT_TEST(unittest.TestCase):
    """A CLASS THAT IS USED TO DEFINE unittests FOR max_integer([..])."""

    def ORD_LIST_TEST(self):
        """A FUNCTION THAT TESTS AN ORDERED LIST OF INTEGERS."""

        ord = [1, 2, 3, 4]
        self.assertEqual(max_integer(ord), 4)

    def UNORD_LIST_TEST(self):
        """A FUNCTION THAT IS USED TO Test an unordered list of integers."""

        unord = [1, 2, 4, 3]
        self.assertEqual(max_integer(unord), 4)

    def MAX_VAL_AT_BEGIN_TEST(self):
        """A FUNCTION THAT TESTS a list with a beginning max value."""

        maxVal_begin = [4, 3, 2, 1]
        self.assertEqual(max_integer(maxVal_begin), 4)

    def EMPTY_LIST_TEST(self):
        """A FUNCTION THAT TESTS an empty list."""

        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def SINGLE_ELEM_LIST_TEST(self):
        """A FUNCTION THAT TESTS a list with a single element."""

        single_elem = [7]
        self.assertEqual(max_integer(single_elem), 7)

    def FLOAT_TEST(self):
        """A FUNCTION THAT TESTS a list of floats."""

        float = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(float), 15.2)

    def INT_FLOAT_TEST(self):
        """A FUNCTION THAT TESTS a list of ints and floats."""

        list_int_float = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(list_int_float), 15.5)

    def STRING_TEST(self):
        """A FUNCTION THAT TESTS a string."""

        str = "Brennan"
        self.assertEqual(max_integer(str), 'r')

    def LIST_OF_STR_TEST(self):
        """A FUNCTION THAT TESTS a list of strings."""

        list_strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(list_strings), "name")

    def EMPTY_STR_TEST(self):
        """A FUNCTION THAT TESTS an empty string."""

        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
