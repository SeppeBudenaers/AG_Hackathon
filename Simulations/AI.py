import requests

url = 'http://127.0.0.1:8080/AI'
response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print('Error:', response.status_code)