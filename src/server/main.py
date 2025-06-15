from server_assign import *

def main():
    try:
        if len(sys.argv) != 2:
            raise ServerError(PORT_MISSING_EXCEPTION)
        port = int(sys.argv[1])
        ip = return_ip()
        new_server = Server(port,ip)
        new_server.bind_server()
    except Exception as error:
        print(f"{error}")

if __name__ == "__main__":
    main()