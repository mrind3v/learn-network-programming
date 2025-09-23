import socket 

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.bind((HOST,PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"connected by {addr}")
        while True: 
            data = conn.recv(1024) 
            if not data:
                break # also break if not data is received
            dataDecoded = data.decode('utf-8') 
            if dataDecoded.lower()=="exit":
                print(f"Closing server as user typed 'exit'...")
                break
            # otherwise just echo back the messages
            # s.sendall(dataDecoded.encode('utf-8'))
            # OR print it
            print(f"Message from Client: {dataDecoded}")
