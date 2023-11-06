#!/usr/bin/python3

"""This python File is Used to Define
an OBJECT ATTRIBUTE function named lookup."""


def lookup(obj):
    """A FUNCTION That is used to Return a list
    of object with it's available attributes."""
    return (dir(obj))
