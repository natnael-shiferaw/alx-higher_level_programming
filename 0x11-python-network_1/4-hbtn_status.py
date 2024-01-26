#!/usr/bin/python3
"""
 A python script that is used to fetch https://alx-intranet.hbtn.io/status
 - It uses the requests package.
"""

import requests

if __name__ == '__main__':
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
