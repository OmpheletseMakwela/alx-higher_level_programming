#!/usr/bin/python3
"""import a module"""
import json
import sys
from os import path
from typing import List
"""A function is defined."""


def save_to_json_file(my_obj: List, filename: str):
    """
    Save a Python object to a file in JSON format.

    Args:
        my_obj (List): Python object to be saved.
        filename (str): Name of the file to save the object.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

def load_from_json_file(filename: str) -> List:
    """
    Load a Python object from a file in JSON format.

    Args:
        filename (str): Name of the file to load the object from.

    Returns:
        List: Loaded Python object.
    """
    with open(filename, 'r') as file:
        return json.load(file)

def add_arguments_to_list(arguments: List[str], filename: str):
    """
    Add all arguments to a Python list and save them to a file in JSON format.

    Args:
        arguments (List[str]): List of arguments to add.
        filename (str): Name of the file to save the list.
    """
    if path.exists(filename):
        # Load the existing list from the file
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    # Add new arguments to the list
    my_list.extend(arguments)

    # Save the updated list to the file
    save_to_json_file(my_list, filename)

if __name__ == "__main__":
    # Extract command-line arguments excluding the script name
    arguments = sys.argv[1:]
    
    # Name of the file to save the list
    filename = 'add_item.json'

    # Add arguments to the list and save it to a file
    add_arguments_to_list(arguments, filename)
