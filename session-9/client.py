import socket

# SERVER IP, PORT

PORT = 8080
IP = "212.128.253.114"


# Create a socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Stablish the connection

s.connect((IP, PORT))

msg = "hola"

# Closing the socket

s.close()

s.send(str.encode(msg))


response = s.recv(2048).decode()

print("Response: {}".format(msg))

s.close()
