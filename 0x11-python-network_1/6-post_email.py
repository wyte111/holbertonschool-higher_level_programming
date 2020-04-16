#!/usr/bin/python3
import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    value = {"email": email}
    req = requests.post(url, data=value)
    print(req.text)
