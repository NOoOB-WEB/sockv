import socket
import time
import sys

ARG_MISSING = "args is missing!"

class ClientError(Exception):
    pass

def argv_handler(arg_length):
    if arg_length == 1:
        raise ClientError(f"\033[91m2 {ARG_MISSING}\033[0m")
    elif arg_length == 2:
        raise ClientError(f"\033[91m1 {ARG_MISSING}\033[0m")
    connection = []


class Client:
    def __init__(self,port,ip):
        self.port = port
        self.ip = ip
        self.client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    def sock_connect(self):
        pass