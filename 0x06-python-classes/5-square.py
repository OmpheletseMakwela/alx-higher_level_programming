#!/usr/bin/python3
"""This module defines a class."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.size ** 2

    def my_print(self):
        """Print the square using '#' characters."""
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print('#' * self.size)
