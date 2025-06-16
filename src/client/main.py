#importing all contents of client_socket
from client_socket import *

def main():
    try:
        argv_handler(len(sys.argv))
    except Exception as error:
        raise error

if __name__ == "__main__":
    main()