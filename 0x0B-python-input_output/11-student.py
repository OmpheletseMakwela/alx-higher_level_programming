#!/usr/bin/python3
"""A class is created."""


class Student:
    """
    Defines a student with first_name, last_name, and age attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
        - attrs (list): List of strings specifying the attributes.

        Returns:
        - dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__

        filtered_attributes = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered_attributes[attr] = getattr(self, attr)
        return filtered_attributes

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
        - json (dict): A dictionary containing attribute.

        Returns:
        - None
        """
        for key, value in json.items():
            setattr(self, key, value)
