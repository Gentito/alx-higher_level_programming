#!/usr/bin/python3
def safe_print_division(a, b):
    """
    A function that divides 2 integers and prints the results.
    """
    c = 0
    try:
        c = a / b
    except (TypeError, ZeroDivisionError):
        c = None
    finally:
        print("Inside result: {}".format(c))
    return c
