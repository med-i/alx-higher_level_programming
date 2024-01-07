#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
and displays the body of the response.
"""

import sys
from urllib import request, parse, error


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            body = response.read().decode()
            print(body)
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
