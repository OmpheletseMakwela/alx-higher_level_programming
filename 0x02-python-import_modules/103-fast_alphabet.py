#!/usr/bin/python3

import sys

alphabet = getattr(__import__("string"), "ascii_uppercase") + "\n"
getattr(sys.stdout, "write")(alphabet)
