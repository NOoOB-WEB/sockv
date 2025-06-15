#importing socket and time which will be used in future
#time is for controlling the server attempts
#sys for reading command-line arguments

import socket
import time
import sys

#defined valuse
SLEEP_TIME = 0.5
PORT_ARG_POSITION = 1
DESIRED_ARG_SIZE = 2

#binding exception when IP and port couldn't be assigned
BINDING_EXCEPTION = "Could not bind server to the desired IP and port !"
#if IP cant be retrieved this error raise
GETTING_IP_EXCEPTION = "Could not get IP address"
#if user can not be retrieved this error raise
GETTING_HOSTNAME_EXCEPTION = "Could not get IP address"
#if user dont enter port or port can not be read, this error raise
PORT_MISSING_EXCEPTION = "You didn't enter port!"
#this exception raise when device is not connected to the router

#this exception raise when socket cant listen to the connections
LISTEN_EXCEPTION = "Can't listen to the desired port and IP: "
#this exception raise when acception can't be happen
ACCEPT_EXCEPTION = "Can't accept connection on the desired port and IP: "

#this class raised theexceptions i wrote
class ServerError(Exception):
    pass

#this function retrieves IP from system
def return_ip():
    try:
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        print(f"IP found: {ip}")
        time.sleep(0.5)
        return ip
    except Exception:
        raise ServerError()

class Server:
    #port and IP will be given to bind the werver on it
    def __init__(self,port,ip):
        self.port = int(port)
        self.ip = ip
        #creating a tcp server(SOCK_STREAM for tcp)
        self.socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #binding given port and IP to the socket
    def bind_server(self):
        try:
            self.socket_server.bind((self.IP,self.port))
            time.sleep(SLEEP_TIME)
        except Exception:
            raise ServerError(BINDING_EXCEPTION) 
        else:
            print(f"Server running {{port: {self.port},IP: {self.ip}}}")
    
    #listening on given port and IP
    def listen_on_server(self):
        try:
            self.socket_server.listen()
        except Exception as error:
            raise ServerError(LISTEN_EXCEPTION + f"{{port:{self.port},IP:{self.ip}}}")
    
    #accepting connection
    def accept_connection(self):
        try:
            conn,addr = self.socket_server.accept()
            return conn,addr
        except Exception as error:
            raise Exception(ServerError(ACCEPT_EXCEPTION + f"{{port:{self.port}, IP{self.ip}}}"))