#!/usr/bin/python3

def uppercase(str):
    print("".join(chr(ord(char) - 32) if "a" <= char <= "z" else char for char in str))
