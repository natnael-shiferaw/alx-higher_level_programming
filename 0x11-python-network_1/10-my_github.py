#!/usr/bin/python3
"""
A python script that takes GitHub credentials(username and password)
and uses GitHub API to display the id.
- uses Basic Authentication with a personal access token as password to
  access the information(only read:user permission if needed)
- First argument will be the username
- Second argument will be the password(in this case, a personal access
  token as passwod)
- It uses the requests and sys packages.
Usage: ./10-my_github.py <GitHub username> <GitHub password>
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
