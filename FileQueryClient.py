from socket import *
 

serverName = "Localhost"
serverPort = 12000
clientSoc = socket(AF_INET, SOCK_STREAM)
clientSoc.connect((serverName,serverPort))
format = "utf-8"


while True:
    command = str(input("Enter a command: "))
    if command == "EXIT":
        clientSoc.send(bytes(command, format))
        break
    if command != "EXIT":
        clientSoc.send(bytes(command, format))
        message = clientSoc.recv(1024)
        message = message.decode()
        print(message)
        
        
        
clientSoc.close()
print("Disconnected from server")

