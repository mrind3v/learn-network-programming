import socket 

def startServer(HOST='127.0.0.1', PORT=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST,PORT))
        while True:
            data, addr = s.recvfrom(1024)
            if not data:
                break 
            dataDecoded = data.decode('utf-8') 
            if dataDecoded.lower() == "exit":
                print("Closing server as the client sent 'exit'...") 
                break 
            # otherwise, just print what's sent by the client 
            print(f"Client message: {dataDecoded}")


if __name__=="__main__":
    startServer()