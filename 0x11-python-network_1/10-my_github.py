#!/usr/bin/python3
"""
This script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""

import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    print(
        response.json().get("id")
        if response.status_code == 200
        else None
    )
