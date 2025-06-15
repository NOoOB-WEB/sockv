import socket
import time
import sys

class ClientError(Exception):
    pass

class Client:
    def __init__(self,port,ip):
        self.port = port
        self.ip = ip
        self.client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)