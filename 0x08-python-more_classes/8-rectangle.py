#!/usr/bin/python3
"""A rectangle class is created."""


class Rectangle:
    """
    Class defining a rectangle.

    Attributes:
        number_of_instances: A class attribute.
        print_symbol: A class attribute.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance with optional width and height.

        Args:
            width (int): The width of the rectangle (default 0).
            height (int): The height of the rectangle (default 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter method to retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method to set the width of the rectangle.

        Args:
            value (int): The value to set as width.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method to retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method to set the height of the rectangle.

        Args:
            value (int): The value to set as height.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """Return a string representation."""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """Print a message."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the biggest rectangle based on the area.

        Args:
            rect_1 (Rectangle): The first instance of Rectangle.
            rect_2 (Rectangle): The second instance of Rectangle.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: The rectangle instance with a bigger or equal area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
