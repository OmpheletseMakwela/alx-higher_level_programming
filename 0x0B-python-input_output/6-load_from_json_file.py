#!/usr/bin/python3
"""import a module"""
import json
"""Define a module"""


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
    - filename (str): The name of the JSON file to load.

    Returns:
    - obj: The object created from the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
