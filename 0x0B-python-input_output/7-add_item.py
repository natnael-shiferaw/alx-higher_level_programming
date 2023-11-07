#!/usr/bin/python3
"""This Python file is used for adding every
arguments to a Python list and finally save to a file."""
import sys

if __name__ == "__main__":

    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        Item = load_from_json_file("add_item.json")
    except FileNotFoundError:
        Item = []

    Item.extend(sys.argv[1:])
    save_to_json_file(Item, "add_item.json")
