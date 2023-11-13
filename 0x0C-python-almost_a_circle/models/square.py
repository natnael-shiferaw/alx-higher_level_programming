#!/usr/bin/python3
"""This is a Python file that is used to define
a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that is used to
    represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """A function that is used to
        initialize a NEW Square.

        Args:
            size (int): represents the size.
            x (int): represents the x coordinate.
            y (int): represents the y coordinate.
            id (int): represents the identity.
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """A function that is used to get or set
        the size of the Square."""

        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """A function that is used to
        update the Square.

        Args:
            *args (ints): It represents NEW attribute values.
                - id attribute represented by 1st argument
                - size attribute represented by 2nd argument
                - x attribute represented by 3rd argument
                - y attribute represented by 4th argument
            **kwargs (dict): represents the NEW key/value
            pairs of attributes.
        """

        if args and len(args) != 0:
            ar = 0

            for arg in args:
                if ar == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg

                elif ar == 1:
                    self.size = arg
                elif ar == 2:
                    self.x = arg
                elif ar == 3:
                    self.y = arg
                ar += 1

        elif kwargs and len(kwargs) != 0:

            for l, c in kwargs.items():

                if l == "id":
                    if c is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = c
                elif l == "size":
                    self.size = c
                elif l == "x":
                    self.x = c
                elif l == "y":
                    self.y = c

    def to_dictionary(self):
        """A function that is used to return
        the representation of a dictionary of a Square."""

        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """A function that is used to return
        representation of the print() and str()
        of the Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
