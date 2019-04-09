import socket

# SERVER IP, PORT
IP = "192.168.1.38"
PORT = 8080

# Loop to ask always the client
while True:
    # Establishing connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    # Making the message separated
    msg = "ATTGCTTAAATCTG\nlen\ncountA"
    if msg == "":
        msg = "empty"


    s.send(str.encode(msg))

    answer = s.recv(2048).decode("utf-8")

    print("Response: {}".format(answer))

    s.close()