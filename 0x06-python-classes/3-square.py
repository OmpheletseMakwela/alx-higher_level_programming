#!/usr/bin/python3
"""This module defines a class."""


class Square:
    """This class represents a class."""
    def __init__(self, size=0):
        """Initialize the square class with a given size."""
        if not isinstance(size,  int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
