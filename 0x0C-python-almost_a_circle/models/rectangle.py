#!/usr/bin/python3
"""This Python file is used to define a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """A class that is used to represent
    a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """A function used to initialize a NEW Rectangle.

        Args:
            width (int): represents the width.
            height (int): represents the height.
            x (int): represents the x coordinate.
            y (int): represents the y coordinate.
            id (int): represents the identity.
        Raises:
            TypeError: If one of them(width/height) isn't an int.
            ValueError: If one of them(width/height) <= 0.
            TypeError: If one of them(x or y) isn't an int.
            ValueError: If one of them(x or y) < 0.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """A function that is used to Set or get
        the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """A function that is used to Set or get
        the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """A function that is used to Set or get
        the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """A function that is used to Set or get
        the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """A function that is used to return
        the AREA of the Rectangle."""
        return self.width * self.height

    def display(self):
        """A function that is used to display/Print
        the Rectangle by using the `#` character."""

        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for k in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for wd in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """A function that is used to
        Update the Rectangle.

        Args:
            *args (ints): It represents NEW attribute values.
                - id attribute represented by 1st argument
                - width attribute represented by 2nd argument
                - height attribute represented by 3rd argument
                - x attribute represented by 4th argument
                - y attribute represented by 5th argument
            **kwargs (dict): represents the NEW key/value
            pairs of attributes.
        """

        if args and len(args) != 0:
            ar = 0

            for arg in args:
                if ar == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg

                elif ar == 1:
                    self.width = arg
                elif ar == 2:
                    self.height = arg
                elif ar == 3:
                    self.x = arg
                elif ar == 4:
                    self.y = arg
                ar += 1

        elif kwargs and len(kwargs) != 0:

            for l, c in kwargs.items():
                if l == "id":
                    if c is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = c
                elif l == "width":
                    self.width = c
                elif l == "height":
                    self.height = c
                elif l == "x":
                    self.x = c
                elif l == "y":
                    self.y = c

    def to_dictionary(self):
        """A function that is used to return
        the representation of a dictionary of a Rectangle."""

        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """A function that is used to return
        representation of the print() and str()
        of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
