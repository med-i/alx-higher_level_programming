#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays the value
of the variable X-Request-Id in the response header.
"""

import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    x_request_id = response.headers.get("X-Request-Id")
    print(x_request_id)
