from socket import *
import sys

BUFFERSIZE = 1024

def main():

    if (len(sys.argv) == 4):
        client(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Please provide a Destination IP Address, port number, and the file to transfer")

def client(IPAddress, port, filepath):

    print(str(serverIP) + ":" + str(serverPort) + " " + str(filepath))
    f = open(str(filepath), "wb")
    while True:
        # establish connection
        port = int(port)
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((IPAddress, port))

        # send & receive
        clientSocket.send(message)
        recvMessage = clientSocket.recv(BUFFERSIZE)
        print("Return text from the server:	", recvMessage, "\n")

        # close connection
        clientSocket.close()