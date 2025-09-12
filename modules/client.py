import socket
import time

PORT = 8000
EXIT_MSG = "--"

class Client:

    def __init__(self, port: str):
        
		# Init class with port
        self.__port: int = port

    def startClient(self):
        time.sleep(1)

        self.__serverIp = str(input("IP: ")) # Input target IP
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Open TCP Connection to server
        self.__client.connect((self.__serverIp, self.__port))

        exit = False


        while not exit:
            time.sleep(0.1) # Prevent server message - Input overlap

            msg = str(input("-: "))
            self.__client.send(msg.encode("utf-8")[:1024])

            response = self.__client.recv(1024)
            response = response.decode("utf-8")

            if response.lower() == EXIT_MSG:
                exit = True

            print(f"Client Recieved: {response}")

        self.__client.close()
        print("Closed connection")
