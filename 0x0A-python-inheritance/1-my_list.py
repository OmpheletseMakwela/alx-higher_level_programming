#!/usr/bin/python3
"""A class is defined."""


class MyList(list):
    def print_sorted(self):
        """
        Prints the list in sorted order (ascending).
        """
        sorted_list = sorted(self)
        print(sorted_list)
