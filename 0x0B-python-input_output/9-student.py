#!/usr/bin/python3

"""This Python file is used to define
a class named Student."""


class Student:
    """A class that is used to
    represent a student."""

    def __init__(self, first_name, last_name, age):
        """A function that is used to
        initialize a NEW Student.

        Args:
            first_name (str): represents the first name.
            last_name (str): represents the last name.
            age (int): represents the age.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A function that is used to get
        a dictionary representation of the Student."""

        return self.__dict__
