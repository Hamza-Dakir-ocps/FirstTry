import sys

import requests


def compute(a, b):
    result = a + b
    return result


def fetch():
    response = requests.get("https://example.com")
    return response.status_code


numbers = [1, 2, 2, 3, 3, 3]
print("Python:", sys.executable)

value = compute(5, 10)
print("Value:", value)

status = fetch()
print("Status:", status)

if True:
    print("bad indent")
