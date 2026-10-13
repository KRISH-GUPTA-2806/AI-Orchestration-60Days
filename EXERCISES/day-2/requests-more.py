import requests


try:
    response = requests.get("https://api.github.com/events",timeout= 10)
    if response.status_code == 200:
        data = response.json()

        print(len(data))
except requests.exceptions.timeout:
    print("Request timed out")
except requests.exceptions.JSONDecodeError:
    print("JSON NOT PARSED")
except requests.exceptions.HTTPError:
    print("http error",response.status_code)