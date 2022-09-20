#!/usr/bin/python3
def remove_char_at(str, n):
    i = str[:n]
    x = str[n+1:]
    return i + x 
