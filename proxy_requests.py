import requests 

# change the ip to the proxy loopback url and port for each protocol
http = "http://127.0.0.1:8080"
https = "https://10.10.1.11:3128"
ftp = "ftp://10.10.1.10:8080"

proxy_dict = {
    "http": http,
    "https": https,
    "ftp": ftp
}

r = requests.get('http://sampleurl.com', proxies=proxy_dict)