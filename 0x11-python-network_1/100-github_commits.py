#!/usr/bin/python3
"""
This script lists 10 last commits of a Github repo.
"""

import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
