#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        upper = ord(str[i])
        if upper >= 97 and upper <= 122:
            upper = upper - 32
        print("{}".format(chr(upper)), end='')
    print()
