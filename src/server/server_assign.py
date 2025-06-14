#importing socket and time which will be used in future
#time is for controlling the server attempts 

import socket
import time

#binding exception when ip and port couldn't be assigned
binding_exception = "Could not bind server to the desired ip and port !"

class ServerError(Exception):
    pass

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
            raise ServerError(binding_exception) 
        else:
            print(f"Server running on port:{self.port} and ip:{self.ip}")