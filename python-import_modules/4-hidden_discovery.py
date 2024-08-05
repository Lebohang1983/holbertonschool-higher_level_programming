#!/usr/bin/python3
import sys
import importlib.util
import os

def main():
    module_path = "/tmp/hidden_4.pyc"


    spec = importlib.util.spec_from_file_location("hidden_4", module_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)



    names = dir(hidden_4)



    names = [name for name in names if not name.startswith("__")]


    names.sort()


    for name in names:
        print(name)


if __name__ == "__main__":
    main()
