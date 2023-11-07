#!/usr/bin/python3

"""This Python file is used to define
a function named to_json_string."""
import json


def to_json_string(my_obj):
    """A function that returns the JSON
    representation of an object (string)."""

    return json.dumps(my_obj)
