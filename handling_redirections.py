import requests

r = requests.post("http://www.github.com")
print(r.url)
print(r.history)
print(r.status_code)