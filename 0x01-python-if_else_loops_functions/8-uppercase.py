#!/usr/bin/python3
def uppercase(str):
    for char in str:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:
            uppercase_ascii = ascii_value - 32
            print("{}".format(chr(uppercase_ascii)), end="")
        else:
            print("{}".format(char), end="")
    print()
