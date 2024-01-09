#!/usr/bin/python3
"""A function is defined."""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line.

    Args:
    - filename (str): The name of the file to modify.
    - search_string (str): The specific string to search.
    - new_string (str): The line of text to insert after each line.

    Returns:
    - None
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
