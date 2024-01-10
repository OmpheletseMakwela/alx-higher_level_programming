#!/usr/bin/python3
"""A function is defined."""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance
    of the specified class.

    Args:
    - obj: Any Python object
    - a_class: The class to check against

    Returns:
    - True if the object is exactly an instance
      of the specified class; False otherwise
    """
    return type(obj) is a_class
