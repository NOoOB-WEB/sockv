#importing all contents of server 
from server_assign import *

#main function will use the server_assign properties to run a server
def main():
    try:
        #checking if user entered port in command_line arguments
        if len(sys.argv) != DESIRED_ARG_SIZE:
            raise ServerError(PORT_MISSING_EXCEPTION)
        #port must be integer
        port = int(sys.argv[PORT_ARG_POSITION])
        ip = return_ip()
        #creating new server socket
        new_server = Server(port,ip)
        new_server.bind_server()
        new_server.listen_on_server()
    except Exception as error:
        print(f"{error}")

if __name__ == "__main__":
    main()