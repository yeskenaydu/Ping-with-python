import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_ip = "192.168.1.102"
server_port = 12345

returnData = "pong"
returnData = bytes(returnData,"utf-8")

server_address = (server_ip , server_port)

print("starting up on ",server_ip," port ", server_port)
sock.bind(server_address)

while True:
    print("\nwaiting to receive message")
    data, address = sock.recvfrom(4096)

    data = data.decode("utf-8")
    
    print ("received ",len(data),"bytes from ",address)
    print ("Message : ",data)
    
    if data:
        sent = sock.sendto(returnData, address)
        print ("sent ", sent, "bytes back to", address)
