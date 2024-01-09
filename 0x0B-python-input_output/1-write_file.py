#!/usr/bin/python3
"""Defines function a function."""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8).

    Args:
    - filename (str): The name of the file to be written.
    - text (str): The string to be written to the file..

    Returns:
    - int: The number of characters written to the file.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        num_characters = file.write(text)
    return num_characters
