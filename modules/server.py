import socket

PORT = 8000
EXIT_MSG = "--"

class Server:

    def __init__(self, serverIP: str, port: str):
        self.__serverIP: str = serverIP
        self.__port: int = port

    def getLocalIp(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
        except Exception:
            ip = "127.0.0.1"
        finally:
            s.close()
        return ip

    def startServer(self):
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Open TCP Connection
        self.__server.bind((self.__serverIP, self.__port))
        self.__server.listen(0)
        print(f"Listening on {self.__serverIP}:{self.__port}")
        print(f"Your local IP: {self.getLocalIp()}")
        clientSocket, clientAddress = self.__server.accept()
        print(f"Accepted connection from {clientAddress[0]}:{clientAddress[1]}")

        exit = False

        while not exit:
            request = clientSocket.recv(1024)
            request = request.decode("utf-8")

            if request.lower() == EXIT_MSG:
                clientSocket.send(EXIT_MSG.encode("utf-8")) # If given exit message, send back to client to confirm server shutdown.
                exit = True
            
            print(f"Server Recieved: {request}")

            response = f"accepted".encode("utf-8")
            clientSocket.send(response)

        clientSocket.close()
        self.__server.close()
