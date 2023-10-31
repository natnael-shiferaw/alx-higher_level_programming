#!/usr/bin/python3
"""THIS FILE DEFINES a locked class."""


class LockedClass:
    """
    A CLASS THAT PREVENTS THE USER FROM instantiating
    new LockedClass attributes for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
