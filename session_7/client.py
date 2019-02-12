# We are programming our first client



import socket

# Create a socket for communicating with the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('socket created')

PORT = 8080
IP = "212.128.253.64"

#Connect to the server

s.connect((IP, PORT))

s.send(str.encode("HOLA CHAVALES"))

msg = s.recv(2048).decode("utf-8")
print("MESSAGE FROM SERVER: ")
print(msg)
s.close()

print('The end')

