import socket
 

 # Have this file always listening to any score updates and change score and ssend to client 
def recfromclient():
    UDP_IP = "127.0.0.1" # this is for the IP address of the second raspberry pi (replace later)
    UDP_PORT = 5005
        # sockets made using UDP communication
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    

    sock.bind((UDP_IP, UDP_PORT))
        
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        return( % data)


sendsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)