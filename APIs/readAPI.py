# 1: import requests
import requests

# 2: define URL
url = "https://official-joke-api.appspot.com/random_joke"

# 3: send and store request
response = requests.get(url)
print(response) # prints the status code

if response.ok:
    # 4: convert response to JSON
    data = response.json()
    print(data)  # prints the entire api
    print()

    # 5: print or use data with specific key
    print(data['setup'])
    print(data['punchline'])
else:
    print(response)