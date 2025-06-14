#importing socket and time which will be used in future
#time is for controlling the server attempts 

import socket
import time

binding_exception = "Could not bind server to the desired ip and port !"

class ServerError(Exception):
    pass

class Server:
    #port and ip will be given to bind the werver on it
    def __init__(self,port,ip):
        self.port = port
        self.ip = ip
        self.socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def bind_server(self):
        try:
            time.sleep(0.5)
            self.socket_server.bind((self.port,self.ip))
        except Exception:
            raise ServerError(binding_exception) 
        