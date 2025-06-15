#importing socket and time which will be used in future
#time is for controlling the server attempts
#sys for reading command-line arguments

import socket
import time
import sys

#binding exception when ip and port couldn't be assigned
BINDING_EXCEPTION = "Could not bind server to the desired ip and port !"
#if ip cant be retrieved this error raise
GETTING_IP_EXCEPTION = "Could not get ip address"
#if user can not be retrieved this error raise
GETTING_HOSTNAME_EXCEPTION = "Could not get ip address"
#if user dont enter port or port can not be read, this error raise
PORT_MISSING_EXCEPTION = "You didn't enter port!"

#this class raised theexceptions i wrote
class ServerError(Exception):
    pass

#this function retrieves ip from system
def return_ip():
    try:
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        print(f"ip found: \nIP:{ip}")
        time.sleep(0.5)
        return ip
    except Exception:
        raise ServerError()

class Server:
    #port and ip will be given to bind the werver on it
    def __init__(self,port,ip):
        self.port = int(port)
        self.ip = ip
        #creating a tcp server
        self.socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #binding given port and ip to the socket
    def bind_server(self):
        try:
            self.socket_server.bind((self.ip,self.port))
            time.sleep(0.5)
        except Exception:
            raise ServerError(BINDING_EXCEPTION) 
        else:
            print(f"Server running on port:{self.port} and ip:{self.ip}")
