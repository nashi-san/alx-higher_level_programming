#!/usr/bin/python3

"""
Python script that takes in a URL,
sends a request to the URL and displays the body of the response
(decoded in utf-8).
"""

import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url)
    req.encoding = "utf-8"
    body = req.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
