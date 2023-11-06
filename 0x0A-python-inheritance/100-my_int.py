#!/usr/bin/python3

"""THIS PYTHON FILE IS USED TO DEFINE
A class MyInt THAT INHERITS FROM int."""


class MyInt(int):
    """USED TO Invert int operators == and !=."""

    def __eq__(self, value):
        """CHANGES == opeartor with != behavior."""

        return self.real != value

    def __ne__(self, value):
        """CHANGES != operator with == behavior."""

        return self.real == value
