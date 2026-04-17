# testing the writeAPI.py file (while the server is running)

import requests

url = "http://127.0.0.1:5000/get-user/0001"
response = requests.get(url)

if response.ok:
    user = response.json()
    print(user['name'] +'\n'+ user['email'])
else:
    print(response.status_code)