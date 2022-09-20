import requests 

custom_header = {'user-agent': 'customUserAgent'}

# r = requests.get('https://samplesite.org', headers=custom_header)

jar = requests.cookies.RequestsCookieJar()
jar.set('cookie_one', 'one', domain='httpbin.org', path='/cookies')
jar.set('cookies_two', 'two', domain='httpbin.org', path='/other')

r = requests.get('https://httpbin.org/cookies', cookies=jar, headers=custom_header)
print(r.text)
print(r.status_code)
print(r.headers['server'])