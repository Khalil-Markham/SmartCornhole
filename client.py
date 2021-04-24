import socket
import struct
    
def send2server(MESSAGE):
        
    UDP_IP = "127.0.0.1" # this part for the second raspberry pi IP address
    UDP_PORT = 5005
    seconds = 2
    seconds = (seconds).to_bytes(8, "little")

    # MESSAGE = b"Hello, World!" - premilary testing
    print("UDP target IP: %s" % UDP_IP)
    print("UDP target port: %s" % UDP_PORT)
    print("message: %s" % MESSAGE)
    # socket made using UDP sockets
    # this sets the timer to 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, seconds)
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))


recvsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    


    
