#!/usr/bin/python3
"""
Displays value of X-Request-Id variable found in header of response.
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        x-request-id = response.getheader('X-Request-Id')

    print(x-request-id)
