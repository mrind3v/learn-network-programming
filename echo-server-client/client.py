import socket 

HOST = "127.0.0.1"  # The server's hostname or IP address again.
PORT = 65432  # The port used by the server again

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT)) 
    #s.sendall(b"Hello World") # send as byte string
    #OR
    message = "Hello World"
    s.sendall(message.encode('utf-8'))
    data = s.recv(1024)

#print(f"Received {data!r}") # as data will by received as byte string
#OR
print(f"Received {data.decode('utf-8')}")
