#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status.
"""

import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    content = response.text
    print("Body response:\n" +
          f"\t- type: {type(content)}\n" +
          f"\t- content: {content}")
