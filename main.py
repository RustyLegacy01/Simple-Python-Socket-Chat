# Modules
import threading 
import time
from modules.server import Server
from modules.client import Client

# Constants (modify at will)
PORT = 8000
EXIT_MSG = "--"

server = Server("127.0.0.1", PORT)
client = Client(PORT)

#######################################################
# This solution uses threading to run the client      #
# and server simultaneously, perhaps using asyncio    #
# could be a better solution if you make this project #
# yourself.                                           #
#######################################################

serverThread = threading.Thread(target=server.startServer)
clientThread = threading.Thread(target=client.startClient)

serverThread.start()
time.sleep(0.5) # Wait time for server startup to finish
clientThread.start()