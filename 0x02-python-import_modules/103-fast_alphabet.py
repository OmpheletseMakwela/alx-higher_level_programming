#!/usr/bin/python3
import sys
getattr(sys.stdout, "write")(getattr(__import__("string"), "ascii_uppercase") + "\n")
