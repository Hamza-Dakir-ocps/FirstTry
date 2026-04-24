import requests


def compute(a, b):
    result = a + b
    return result


def fetch():
    response = requests.get("https://example.com")
    return response.status_code
