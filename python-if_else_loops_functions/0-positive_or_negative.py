#!/usr/bin/python3
import random
number = random.randint(-10, 10)

for x in range(-10, 10):
    if x > 0:
        print(f"{number}, is positive")
    if x == 0:
        print(f"{number}, is zero")
    if x < 0:
        print(f"{number}, is negative")
