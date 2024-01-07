#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""

import sys
from urllib import request


if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        headers = response.getheaders()
        x_request_id = dict(headers).get("X-Request-Id")
        print(x_request_id)
