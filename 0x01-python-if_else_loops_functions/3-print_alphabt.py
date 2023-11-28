#!/usr/bin/python3
import sys

alphabet = ''.join(chr(i) for i in range(97, 123) if chr(i) not in ['q', 'e'])
output_string = "{}".format(alphabet)

print(output_string, end='')
