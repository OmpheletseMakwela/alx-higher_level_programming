#!/usr/bin/python3
"""A function is defined."""


def class_to_json(obj):
    """
    Returns a dictionary description for JSON serialization of an object.

    Args:
    - obj: An instance of a Class with serializable attributes.

    Returns:
    - dict: Dictionary description of the object's serializable attributes.
    """
    json_dict = {}
    attributes = obj.__dict__

    for attr_name, attr_value in attributes.items():
        if isinstance(attr_value, (list, dict, str, int, bool)):
            json_dict[attr_name] = attr_value

    return json_dict
