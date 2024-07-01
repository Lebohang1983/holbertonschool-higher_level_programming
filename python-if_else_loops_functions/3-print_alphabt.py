#!/usr/bin/python3

for alpha in range(97, 123):
    if alpha not in [ord('q'), ord('e')]:
        print("{}".format(chr(alpha)), end="")
