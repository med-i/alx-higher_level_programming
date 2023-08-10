#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv
    args_count = len(args)

    if args_count == 1:
        print("0 arguments.")
    else:
        print(
            "{} {}:".format(
                args_count - 1, "argument" if args_count == 2 else "arguments"
            )
        )
        for i, arg in enumerate(args[1:], 1):
            print(f"{i}: {arg}")
