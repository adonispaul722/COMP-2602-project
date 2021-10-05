from socket import *

#Creating server Socket
serverPort = 12345
host = ('127.0.0.1')
serverSoc = socket.socket()
serverSoc = socket(AF_INET,SOCK_STREAM)
serverSoc.bind = (host,serverPort)
format = "utf-8"


print("[STARTED] Server is started...")
serverSoc.listen(10)
print("[LISTENING] The Server is running. Waiting for a command...")

def putFunction():
    file = open ("data.txt", "r")
    data = file.read




def userCommand(command):
    print("The command entered was " + command)
    if (command == "PUT"):
        putfunction()



while 1:

    connectionSocket, address = serverSoc.accept()
    command = connectionSocket.recv(1024)
    userCommand()






def main():
    
    