#!/usr/bin/python3
import importlib
if __name__ == "__main__":
    import hidden_4
    for name in dir(hidden_4):
        if not name.startswith("__"):
            print(name)
