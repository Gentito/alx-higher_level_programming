#!/usr/bin/python3
for i in range(0, 10):
    for x in range(i + 1, 10):
        if (not (i == 8 and x == 9)):
            print("{}{}".format(i, x), end=", ")
        else:
            print("{}{}".format(i, x))
