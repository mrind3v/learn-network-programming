import socket 

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

# since socket.socket() function creates an object that supports the context manager type, we can use it
# with the "with statement" so as to close to object after with ends (clean up the object)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    # step1 - bind to ip and port 
    s.bind((HOST,PORT)) 

    # step2 - enables server to accept connections -> server becomes a listening socket
    # listen() has an optional param that denotes -> number of unaccepted connections that server will allow
    # before refusing any new connection -> OR length of the queue of pending connections
    s.listen() 

    # step3 - accept connection from client. The accept() function is a blocking call (similar to async fns).
    # Meaning, it's an I/O heavy operation since it waits for the client. Then returns a new socket object and
    # a tuple (host,port) holding addr of the client
    conn, addr = s.accept()

    # step4 - since conn is another socket object which need to be cleaned up after our work is done. We shall
    # open another with statement so it is automatically closed
    with conn:
        print(f"connected by {addr}")

        # step5 - infinite while loop over the blocking call recv() because it is also an I/O heavy operation
        # -> waits for client to send something
        while True:
            data = conn.recv(1024) # max number of bytes to receive from client in one call
            
            # step6 - if client sends an empty byte object b'' -> client closed the connection. So break 
            # out of the loop
            if not data:
                break

            # step7 (Q specific) - we shall echo back what the client has sent to the client
            conn.sendall(data)