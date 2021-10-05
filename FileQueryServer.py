from socket import *


serverPort = 12000
host="Localhost"
serverSoc = socket(AF_INET,SOCK_STREAM)
serverSoc.bind((host,serverPort))

serverSoc.listen(1)
format = "utf-8"


print("[STARTED] Server is started...")
serverSoc.listen(10)
print("[LISTENING] The Server is running. Waiting for a command...")

connectionSocket, address = serverSoc.accept()



def putFunction(file):
    message="PUT CALLED"
    connectionSocket.send(message.encode())
def createFunction(file):
    message="CREATE CALLED"
    connectionSocket.send(message.encode())
def listFunction():
    message="LIST CALLED"
    connectionSocket.send(message.encode()) 
def showFunction(file):
    message="SHOW CALLED"
    connectionSocket.send(message.encode())
def deleteFunction(file):
    message="DELETE CALLED"
    connectionSocket.send(message.encode())
def wordcountFunction(file):
    message="WORDCOUNT CALLED"
    connectionSocket.send(message.encode())
def searchFunction(file):
    message="SEARCH CALLED"
    connectionSocket.send(message.encode())




while True:
    command = connectionSocket.recv(1024)
    command = command.decode()
    command = command.split()
    if command[0]=="PUT":
        putFunction(command[1])
    if command[0]=="CREATE":
        createFunction(command[1])
    if command[0]=="LIST":
        listFunction()
    if command[0]=="SHOW":
        showFunction(command[1])
    if command[0]=="DELETE":
        deleteFunction(command[1])
    if command[0]=="WORDCOUNT":
        wordcountFunction(command[1])
    if command[0]=="SEARCH":
        searchFunction(command[1])
    if command[0]=="EXIT":
        message="Disconnected from server"
        connectionSocket.send(message.encode())
        break
   


connectionSocket.close()











    
