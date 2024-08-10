#!/usr/bin/python3
import importlib.util
import sys
import os

def main():
    module_path = "/tmp/hidden_4.pyc"



    if not os.path.exists(module_path):
        print(f"Error: The file {module_path} does not exist.")
        return
    
    module_name = os.path.splitext(os.path.basename(module_path))[0]
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    names = sorted(name for name in dir(module) if not name.startswith("__"))

    for name in names:
        print(name)

if __name__ == "__main__":
    main()
