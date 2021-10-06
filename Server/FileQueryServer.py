from socket import *
import os


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
    message = os.path.dirname(__file__)
    connectionSocket.send(message.encode())
def createFunction(file):
    f = open(file,"a").close
    message="Enter File Contents: "
    connectionSocket.send(message.encode())
    line = connectionSocket.recv(1024)
    line = line.decode()
    with open(file,"w") as f:
        f.write(line)
def listFunction():
    message="LIST CALLED"#####
    connectionSocket.send(message.encode()) 
def showFunction(file):
    message="SHOW CALLED"#####
    connectionSocket.send(message.encode())
def deleteFunction(file):
    message="DELETE CALLED"#####
    connectionSocket.send(message.encode())
def wordcountFunction(file):
    message="WORDCOUNT CALLED"####
    connectionSocket.send(message.encode())
def searchFunction(file):
    message="Enter word to search for: "
    connectionSocket.send(message.encode())
    wordKey = connectionSocket.recv(1024)
    wordKey= wordKey.decode()
    f = open(file,"r")
    found=False
    for line in f:
        for word in line.split():
            if word==wordKey:
                message=("%s was found in %s"%(wordKey,file))
                found=True
    if found==False:
        message=("%s was not found in %s"%(wordKey,file))
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











    
