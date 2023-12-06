#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

if len(argv) == 1:
    print("0 arguments.")
else:
    count = len(argv) - 1
    plural = "s" if count > 1 else ""
    print("{:d} argument{}:".format(count, plural))
    for i in range(1, len(argv)):
        print("{:d}: {}".format(i, argv[i]))
