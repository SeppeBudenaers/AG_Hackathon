import requests

url = 'http://127.0.0.1:8080/?start_date=2024-01-01 00:00:00&end_date=2024-12-31 0:00:00'

response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print('Error:', response.status_code)