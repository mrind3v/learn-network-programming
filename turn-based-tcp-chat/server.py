import socket 
"""
An Interactive, turn-based TCP chat application where the client always starts first,
and then messages alternate between client and server.
"""

# FOR SERVER - RECEIVE -> PRINT -> RESPOND
def startServer(HOST='127.0.0.1', PORT=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
        s.bind((HOST,PORT)) 
        s.listen() 
        conn, addr = s.accept()
        with conn:
        # print this message as long as connection is active
            print(f"connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data: 
                    break 
                dataDecoded = data.decode('utf-8')  
                print(f"Message from Client: {dataDecoded}") 
                if dataDecoded.lower() == "exit":
                    print(f"Closing server as client sent 'exit'...") 
                    break
                response = input("Enter response to client: ") 
                # use the client "conn" socket object to send response!
                conn.sendall(response.encode('utf-8')) 


if __name__ == "__main__":
    startServer()