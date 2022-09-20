import requests

payload = {'user_name': 'admin', 'password': 'password'}
r = requests.get('http://httpbin.org/get', params=payload)

print(r.url)
print(r.text)