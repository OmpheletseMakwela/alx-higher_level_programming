#!/usr/bin/python3
"""A function is defined."""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if it is an instance
    of a class that inherited from,
    the specified class.

    Args:
    - obj: Any Python object
    - a_class: The class to check against

    Returns:
    - True if the object is an instance of, or if it is an instance
      of a class that inherited from,
      the specified class; False otherwise
    """
    return isinstance(obj, a_class)
