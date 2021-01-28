from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

while True:
    print("Ready to serve")
    connectionSocket, addr = // TODO
    try:
        message = '' // TODO
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = '' // TODo
        # send one HTTP header line into socket
        # send  content of requested file to client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # send file not found error
        # close client socket
serverSocket.close()
sys.exit()
