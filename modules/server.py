import socket
import time

PORT = 8000
EXIT_MSG = "--"

class Server:

    def __init__(self, serverIP: str, port: str):
        self.__serverIP: str = serverIP
        self.__port: int = port

    def startServer(self):
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind((self.__serverIP, self.__port))
        self.__server.listen(0)
        print(f"Listening on {self.__serverIP}:{self.__port}")
        clientSocket, clientAddress = self.__server.accept()
        print(f"Accepted connection from {clientAddress[0]}:{clientAddress[1]}")

        exit = False

        while exit == False:
            request = clientSocket.recv(1024)
            request = request.decode("utf-8")

            if request.lower() == EXIT_MSG:
                clientSocket.send(EXIT_MSG.encode("utf-8"))
                exit = True
            
            print(f"Server Recieved: {request}")

            response = f"accepted".encode("utf-8")
            clientSocket.send(response)

        clientSocket.close()
        self.__server.close()
