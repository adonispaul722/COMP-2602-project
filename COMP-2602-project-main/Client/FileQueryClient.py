from socket import *
import os
import shutil

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
        command = command.split()
        if command[0]=="PUT":
            message = clientSoc.recv(1024)
            message = message.decode()
            dst_path = message
            dst_path = dst_path.__add__("\\")
            dst_path = dst_path.__add__(command[1])
            src_path = os.path.dirname(__file__)
            src_path = src_path.__add__("\\")
            src_path = src_path.__add__(command[1])
            shutil.move(src_path, dst_path)

        if command[0]=="CREATE":
            message = clientSoc.recv(1024)
            message = message.decode()
            line=str(input(message))
            clientSoc.send(bytes(line, format))
        
        if command[0]=="SEARCH":
            message = clientSoc.recv(1024)
            message = message.decode()
            wordKey=str(input(message))
            clientSoc.send(bytes(wordKey, format))
            message = clientSoc.recv(1024)
            message = message.decode()
            print(message)

        if command[0]=="LIST":
            message = clientSoc.recv(1024)
            message = message.decode()
            print(message)
        
        if command[0]=="WORDCOUNT":
            message = clientSoc.recv(1024)
            message = message.decode()
            print(message)

        if command[0]=="SHOW":
            message = clientSoc.recv(1024)
            message = message.decode()
            print(message)

        if command[0]=="DELETE":
            message = clientSoc.recv(1024)
            message = message.decode()
            print(message)

clientSoc.close()
print("Disconnected from server")

