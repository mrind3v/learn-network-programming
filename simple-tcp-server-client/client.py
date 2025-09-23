import socket 

# server host ip 
HOST = '127.0.0.1'
# server port 
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.connect((HOST,PORT)) 
    while True: 
        inputStr = input("Enter your message: ")
        # we need to close both server and client if the client types in "exit"
        # first send the message anyway to server (the message can be exit as well) - so server can close itself
        s.sendall(inputStr.encode('utf-8'))
        # then close client if its the exit message
        if inputStr.lower()=="exit":
            print("Closing connection...") 
            break
