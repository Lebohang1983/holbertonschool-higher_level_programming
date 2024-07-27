#!/usr/bin/python3
import sys

if __name__ == "__main__":
    number = len(sys.argv) - 1
    if number == 1:
        print(f"{number} argument:")
    elif number > 1:
        print(f"{number} arguments:")
    else:
        print(f"{number} arguments.")
    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[i]}")
