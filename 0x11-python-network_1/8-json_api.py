#!/usr/bin/python3
"""A python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
- The letter is sent in the variable q
- If no argument is given, sets `q=""`
- If the response body is in JSON format and not empty:
    displays the id and name
- It uses the requests and sys packages.

Usage: ./8-json_api.py <letter>
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print(f'[{response.get("id")}] {response.get("name")}')
    except ValueError:
        print("Not a valid JSON")
