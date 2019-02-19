import socket

PORT = 8080
IP = "212.128.253.114"
MAX_OPEN_REQUEST = 5


def process_client(cs):



    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")

    print("Message from the client: {}".format(msg))

    # Sending the msg back to the client as we are an echo server

    cs.send(str.encode(msg))
    cs.close()


# Create a socket for connecting to the clients

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))    # it is only one parameter but we write two parenthesis bc there is a tupple inside

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))

while True:


    print("Waiting for connections at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()


     #-- processing the client request

    print("Attending client: {}".format(address))



    process_client(clientsocket)



