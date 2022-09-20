import requests

r = requests.get('http://httpbin.org/get')
response = r.json()
print(response['args'])
print(response['headers'])
print(response['headers']['Accept'])
print(response['headers']['Accept-Encoding'])
# print(response['headers']['Connection'])
print(response['headers']['Host'])
print(response['headers']['User-Agent'])
print(response['origin'])
print(response['url'])

print(r.headers['Access-Control-Allow-Credentials'])
print(r.headers['Access-Control-Allow-Origin'])
print(r.headers['CONNECTION'])
print(r.headers['content-length'])
print(r.headers['Content-Type'])
print(r.headers['Date'])
print(r.headers['server'])
# via header 
# print(r.headers['via']) 
