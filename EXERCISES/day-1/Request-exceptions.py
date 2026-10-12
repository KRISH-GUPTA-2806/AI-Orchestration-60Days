
#exception handling for API


import requests

try:
    response = requests.get("https://www.google.com",timeout=10)
    if response.status_code == 200:
        print("SUCCESS")
except requests.exceptions.HTTPError:
    print("HTTP REQUEST UNSUCCESSFUL")
except requests.exceptions.Timeout:
    print("REQUEST TIMED OUT")
except requests.exceptions.JSONDecodeError:
    print("REQUEST JSON TIMED OUT")
except requests.exceptions.RequestException:
    print("REQUEST FAILED")

