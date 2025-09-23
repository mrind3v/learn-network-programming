import socket 

def startClient(HOST='127.0.01', PORT=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: 
        while True:
            message = input("Enter message: ") 
            s.sendto(message.encode('utf-8'), (HOST,PORT)) 
            if message.lower()=="exit":
                print(f"Closing connection...") 
                break 



if __name__ == "__main__":
    startClient()