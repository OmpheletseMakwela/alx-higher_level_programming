#!/usr/bin/python3
"""defines a funciton"""


def read_file(filename=""):
    """
    Reads the content of a text file (UTF-8) and prints it to stdout.

    Args:
    - filename (str): The name of the file to be read.

    Returns:
    - None

    Note: This function uses the 'with' to open the file, print its content.
    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end='')
