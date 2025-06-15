#importing socket and time which will be used in future
#time is for controlling the server attempts
#sys for reading command-line arguments
from system import OS
import socket
import time
import sys
import subprocess

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

os_detector = OS()

OPERATING_SYSTEM = os_detector.determine_os()

#These functions retrieves IP from system(Windows_unix-based)
def return_ip_windows():
    try:
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        print(f"IP found: {ip}")
        time.sleep(0.5)
        return ip
    except Exception:
        raise ServerError()

def return_ip_unix():
    try:
        # TCP “connect” to a public DNS server — the OS will pick the
        # appropriate outbound interface and source IP for that route.
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
        sock.close()
        print(f"IP found: {ip}")
        time.sleep(SLEEP_TIME)
        return ip
    except Exception as ex:
        raise ServerError(f"Could not get non‑loopback IP: {ex}")

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
            self.socket_server.bind((self.ip,self.port))
            time.sleep(SLEEP_TIME)
        except Exception:
            raise ServerError(BINDING_EXCEPTION) 
        else:
            print(f"Server running {{port: {self.port},IP: {self.ip}}}")
    
    #listening on given port and IP

    def listen_on_server(self):
        try:
            self.socket_server.listen()
            time.sleep(SLEEP_TIME)
            print(f"Listening on{{port: {self.port},IP: {self.ip}}}")
        except Exception:
            raise ServerError(LISTEN_EXCEPTION + f"{{port:{self.port},IP:{self.ip}}}")
    
    #accepting connection(conn for reading and writing file from client and add for getting client addr which contains port and IP)
    #conn for reading and writing file from client and add for getting client addr which contains port and IP

    def accept_connection(self):
        try:
            conn,addr = self.socket_server.accept()
            return conn,addr
        except Exception:
            raise Exception(ServerError(f"{ACCEPT_EXCEPTION} {{port:{self.port}, IP{self.ip}}}"))
    