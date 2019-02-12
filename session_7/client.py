# We are programming our first client



import socket

# Create a socket for communicating with the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('socket created')

PORT = 8080
IP = "212.128.253.64"

s.connect((IP, PORT))

print('The end')

