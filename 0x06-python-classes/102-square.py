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
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.size ** 2

    def __eq__(self, other):
        """Override the equality comparison."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Override the inequality comparison."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Override the less-than comparison."""
        return self.area() < other.area()

    def __le__(self, other):
        """Override the less-than-or-equal-to comparison."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Override the greater-than comparison."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Override the greater-than-or-equal-to comparison."""
        return self.area() >= other.area()
