#!/usr/bin/python3

"""THIS PYTHON FILE CONTAINS A Module Mylist
THAT IS USED TO CREATE A CLASS THAT INHERITS
FROM THE list class"""


class MyList(list):
    """A Class NAMED MyList THAT
    INHERITS FROM list"""

    def print_sorted(self):
        """A FUNCTION THAT IS USED TO PRINT
        THE list, IN ASCENDING ORDER."""

        newlist = self[:]
        newlist.sort()
        print("{}".format(newlist))
