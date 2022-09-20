import requests 

first_session = requests.Session()

first_session.cookies.update({'default_cookie': 'default'})

r = first_session.get('http://httpbin.org/cookies', cookies={'first-cookie': '111'})
print(r.text)

r = first_session.get('http://httpbin.org/cookies')
print(r.text)