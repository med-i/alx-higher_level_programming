#!/usr/bin/python3
import hidden_4 as names

if __name__ == "__main__":
    for name in dir(names):
        if name[:2] != "__":
            print(name)
