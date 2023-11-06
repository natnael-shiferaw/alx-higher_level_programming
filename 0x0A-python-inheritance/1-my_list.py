#!/usr/bin/python3
"""THIS PYTHON FILE CONTAINS THE Module Mylist
THAT CREATES A class THAT INHERITS FROM list class
"""


class MyList(list):
    """A Class MyList INHERITS FROM list"""

    def print_sorted(self):
        """A FUNCTION THAT IS USED TO PRINT
        THE list, IN ASCENDING ORDER"""

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
