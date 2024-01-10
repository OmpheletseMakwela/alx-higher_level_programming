#!/usr/bin/python3
"""A class is defined."""


class MyList(list):
    """A function is defined."""
    def print_sorted(self):
        """
        Prints the list in sorted order (ascending).
        """
        sorted_list = sorted(self)
        print(sorted_list)
