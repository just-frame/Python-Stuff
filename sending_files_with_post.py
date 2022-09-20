import requests

url = 'http://httpbin.org/post'
file_list = [
    ('image', ('image1.jpg', open('image1.jpg', 'rb'), 'image/png')),
    ('image', ('image2.jpg', open('image2.jpg', 'rb'), 'image/png'))
]

r = requests.post(url, files=file_list)
print(r.text)