#!/usr/bin/python3
"""import a module."""
import json
"""A function is defined"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
    - my_obj: The object to be converted to a JSON string.

    Returns:
    - str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
