import requests

first_session = requests.Session()
second_session = requests.Session()

first_session.get('http://httpbin.org/cookies/set/cookieone/111')
r = first_session.get('http://httpbin.org/cookies')
print(r.text)

second_session.get('http://httpbin.org/cookies/set/cookietwo/222')
r = second_session.get('http://httpbin.org/cookies')
print(r.text)

r = first_session.get('http://httpbin.org/anything')
print(r.text)

print(r.status_code)
print(r.headers['server'])