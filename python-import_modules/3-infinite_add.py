#!/usr/bin/python3
import sys
def add_all(*args):
    return sum(args)

if __name__ == "__main__":

    numbers = map(int, sys.argv[1:])
    result = add_all(*numbers)
    print(result)
