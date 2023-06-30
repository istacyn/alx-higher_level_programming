#!/usr/bin/python3
"""
Takes in a URL and an email address,
sends POST request to passed URL with email as parameter
Displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
