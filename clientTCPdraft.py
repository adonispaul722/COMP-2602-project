from socket import *
import sys 

#Creating client Socket
clientPort = 12345
host = ('127.0.0.1')
clientSoc = socket.socket()
clientSoc = socket(AF_INET,SOCK_STREAM)
clientSoc.connect= ((host,clientPort))
format = "utf-8"


def mainCode():
    command = str(input("Enter a command: "))
    clientSoc.send(bytes(command, format))




