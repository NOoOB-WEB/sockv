from server_assign import *

def main():
    try:
        if len(sys.argv) != DESIRED_ARG_SIZE:
            raise ServerError(PORT_MISSING_EXCEPTION)
        port = int(sys.argv[PORT_ARG_POSITION])
        ip = return_ip()
        new_server = Server(port,ip)
        new_server.bind_server()
    except Exception as error:
        print(f"{error}")

if __name__ == "__main__":
    main()