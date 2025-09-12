import socket
import threading 
import time
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout

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

class Client:

    def __init__(self, port: str):
        
        self.__port: int = port

    def startClient(self):
        time.sleep(1)

        self.__serverIp = str(input("IP: "))
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__client.connect((self.__serverIp, self.__port))

        exit = False

        while exit == False:
            msg = str(input("-: "))
            self.__client.send(msg.encode("utf-8")[:1024])

            response = self.__client.recv(1024)
            response = response.decode("utf-8")

            if response.lower() == EXIT_MSG:
                exit = True

            print(f"Client Recieved: {response}")

        self.__client.close()
        print("Closed connection")



server = Server("127.0.0.1", PORT)
client = Client(PORT)

serverThread = threading.Thread(target=server.startServer)
clientThread = threading.Thread(target=client.startClient)

serverThread.start()
time.sleep(0.5)
clientThread.start()