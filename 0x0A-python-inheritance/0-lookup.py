#!/usr/bin/python3
"""A function is defined."""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
    - obj: Any Python object

    Returns:
    - A list of strings
    """
    return dir(obj)
