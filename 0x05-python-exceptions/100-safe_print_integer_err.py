#!/usr/bin/python3
from sys import stderr
def safe_print_integer_err(value):
    """
    A function that prints an integer.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError) as e:
        stderr.write("Exception: {}\n".format(e))
        return (False)
