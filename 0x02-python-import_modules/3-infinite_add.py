#!/usr/bin/python3
import sys

if __name__ == "__main__":
    numbers = sys.argv
    result = 0

    for number in numbers[1:]:
        result += int(number)

    print(result)
