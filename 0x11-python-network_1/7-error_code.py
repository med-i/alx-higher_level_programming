#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
and displays the body of the response.
"""

import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(
        f"Error code: {response.status_code}"
        if response.status_code >= 400
        else response.text
    )
