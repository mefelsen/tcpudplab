from socket import *
import sys

BUFFERSIZE = 1024

def main():

    if (len(sys.argv) == 2):
        server(sys.argv[1])
    else:
        print("Please provide a port number")

def server(port):

    # establish connection
    port = int(port)
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', port))
    serverSocket.listen(1)

    while True:

        # receive & send
        connectionSocket, address = serverSocket.accept()
        message = connectionSocket.recv(BUFF_SIZE)
        connectionSocket.send(message)

        # close connection
        connectionSocket.close()