# this script assumes the connection will always succeed...
# and that the server ALWAYS expects a client to send data first (some servers send data to clients/you and await your response)
# third assumption is that server will always send data back within an expected window of time

import socket

target_host = "www.google.com"
target_port = 443

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client 
client.connect((target_host,target_port))

# send some data # GET, OPTIONS, POST, PUT request etc
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receive some data
response = client.recv(4096)

print(response)
