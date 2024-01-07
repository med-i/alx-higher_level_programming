#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response.
"""

import sys
from urllib import request, parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = parse.urlencode({'email': email})
    data = data.encode()
    req = request.Request(url, data)

    with request.urlopen(req) as response:
        body = response.read().decode()
        print(body)
