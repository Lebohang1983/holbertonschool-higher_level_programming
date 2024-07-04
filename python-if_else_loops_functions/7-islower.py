#!/usr/bin/python3

def islower(c):
    if ord('a') <= ord(c) <= ord('z'):
        return True
    else:
        return False

print(islower('a'))
print(islower('Z'))
print(islower('m'))
