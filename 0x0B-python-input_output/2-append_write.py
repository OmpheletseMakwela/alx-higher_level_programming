#!/usr/bin/python3
"""A function is defined."""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file and returns the number

    Args:
    - filename (str): The name of the file to which text will be appended.
    - text (str): The string to be appended to the file.

    Returns:
    - int: The number of characters added to the file.
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        num_characters_added = file.write(text)
    return num_characters_added
