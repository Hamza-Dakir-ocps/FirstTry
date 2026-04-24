import sys
from collections import Counter
from datetime import datetime

import requests


def compute(a, b):
    result = a + b
    return result


def fetch():
    response = requests.get("https://example.com")
    return response.status_code


def stats(nums):
    return Counter(nums)


def format_time():
    return datetime.now().strftime("%Y-%m-%d")


value = compute(5, 10)
print("Value:", value)

status = fetch()
print("Status:", status)

print(stats(numbers))

print(format_time())

if True:
    print("bad indent")
