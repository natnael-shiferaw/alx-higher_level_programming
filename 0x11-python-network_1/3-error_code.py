#!/usr/bin/python3
"""
A python script that is used to take in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
- manages urllib.error.HTTPError exceptions and print : Error code:
    followed by the HTTP status code.
- It uses the urllib and sys packages.
"""

import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]

    own_request = request.Request(url)
    try:
        with request.urlopen(own_request) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
