#!/usr/bin/python3
"""Import a module"""
import json
"""A function is defined."""


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
    - my_obj: The object to be written to the file.
    - filename (str): The name of the file to save the JSON representation.

    Returns:
    - None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
