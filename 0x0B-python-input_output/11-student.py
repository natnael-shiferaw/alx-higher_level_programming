#!/usr/bin/python3

"""This Python file is used to Define
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

    def to_json(self, attrs=None):
        """A function used to get a dictionary
        representation of the Student.

        Args:
            attrs (list): (Optional) represents the attributes.
        """

        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__

    def reload_from_json(self, json):
        """A fucntion that is used to replace
        every attributes Student.

        Args:
            json (dict): represents the key/value
            pairs that replace the attributes.
        """

        for i, j in json.items():
            setattr(self, i, j)
