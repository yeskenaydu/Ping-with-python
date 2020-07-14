import random
from socket import *
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',12345))
while True:
    rand = random.randint(0,10)
    message,address=serverSocket.recvfrom(4096)
    message = message.upper()
    print("[",message,"]")
    
    if (message.decode().startswith("PING")):
        serverSocket.sendto("pong".encode(), address)
    
