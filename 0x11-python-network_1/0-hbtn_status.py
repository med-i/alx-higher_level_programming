#!/usr/bin/python3
"""
This script fetches a URL
"""

import urllib

URL = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
    with urllib.request.urlopen(URL) as response:
        body = response.read()
        print("Body response:\n"+
                f"\t- type: {type(body)}\n"+
                f"\t- content: {body}\n"+
                f"\t- utf8 content: {body.decode()}")
    

