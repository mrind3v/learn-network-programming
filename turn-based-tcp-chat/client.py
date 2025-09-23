import socket 

def startClient(HOST='127.0.0.1', PORT='65432'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
        s.connect((HOST,PORT))
        while True:
            message = input("Enter message to server: ") 
            s.sendall(message.encode('utf-8')) 
            if message.lower() == "exit":
                print("Closing connection...") 
                break 
            # wait for server response
            serverMessage = s.recv(1024)
            if not serverMessage:
                print("Server disconnected") 
            serverMessageDecoded = serverMessage.decode('utf-8') 
            print(f"Response from server: {serverMessageDecoded}")  



if __name__ == "__main__":
    startClient()