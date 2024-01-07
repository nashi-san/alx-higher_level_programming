#!/usr/bin/python3
""" Python script that that takes in a URL, sends a request
to the URL and displays the value of the X-Request-Id variable
found in the header of the response.
"""
import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    header = response.info()
    req_id = header.get("X-Request-Id")
    print(req_id)
