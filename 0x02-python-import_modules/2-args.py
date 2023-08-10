#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv
    args_count = len(args)

    if args_count == 1:
        print("0 arguments.")
    else:
        print(f"{args_count - 1} arguments:")
        for i, arg in enumerate(args[1:], 1):
            print(f"{i}: {arg}")
