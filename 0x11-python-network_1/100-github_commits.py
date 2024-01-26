#!/usr/bin/python3
"""
A python script that takes 2 arguments:
    - first argument is the repository name
    - second argument is the owner name
- lists 10 commits(from the most recent to oldest) of the
  repository "rails" by the user "rails". It uses the GitHub API.
  -Here is the documentation https://developer.gitub.com/v3/repos/commits
  - print all commits by: `<sha>: <author name>` (one by line)
- It uses the requests and sys packages.
Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import requests
import sys


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"

    response = requests.get(url)
    commits = response.json()
    try:
        for n in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
