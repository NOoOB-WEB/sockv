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
        print(f"Operating System: {OPERATING_SYSTEM}")
        if OPERATING_SYSTEM == "Windows":
            ip = return_ip_windows()
        else:
            ip = return_ip_unix()
        #creating new server socket
        new_server = Server(port,ip)
        new_server.bind_server()
        new_server.listen_on_server()
        conn,addr = new_server.accept_connection()

        with conn:
            while True:
                data = conn.recv(1024)
                #we will get the name of the client later
                print(f"user:{data.decode()}")
                if data.decode() == "EXIT":
                    break
    except Exception as error:
        print(f"\033[91m{error}")
    finally:
        new_server.socket_server.close()

if __name__ == "__main__":
    main()