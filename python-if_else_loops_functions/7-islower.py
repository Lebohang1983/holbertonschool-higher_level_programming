#!/usr/bin/python3

def is_lower(c):
    if ord('a') <= ord(c) <= ord('z'):
        return True
    else:
        return False
print(is_lower('a'))
print(is_lower('Z'))
