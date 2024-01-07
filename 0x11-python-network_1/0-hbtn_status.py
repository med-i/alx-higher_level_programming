#!/usr/bin/python3
"""
Task 0
"""

from urllib import request

URL = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
    with request.urlopen(URL) as response:
        body = response.read()
        print("Body response:\n"+
                f"\t- type: {type(body)}\n"+
                f"\t- content: {body}\n"+
                f"\t- utf8 content: {body.decode()}")
    

