import requests

payload = {'user_name': 'admin', 'password': 'password'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.url)
print(r.text)