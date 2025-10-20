# the client.py will still exist
import socket
import threading
from concurrent.futures import ThreadPoolExecutor

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
MAX_WORKERS = 5     # The maximum number of threads in the pool

def handle_client(conn, addr):
    """
    This function is executed by each thread in the pool.
    It handles the communication with a single client.
    """
    print(f"Connected by {addr} using thread {threading.get_ident()}")
    with conn:
        while True:
            # Receive data from the client (up to 1024 bytes)
            data = conn.recv(1024)
            if not data:
                print(f"Client {addr} disconnected.")
                break

            data_decoded = data.decode('utf-8')

            if data_decoded.lower().strip() == "exit":
                print(f"Client {addr} requested to close the connection.")
                break
            
            conn.sendall(data)
    
    print(f"Closing connection for {addr}.")


def start_server():
    """
    Starts the server, listens for incoming connections,
    and submits each new client to the thread pool.
    """
    # Create a server socket using IPv4 and TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print(f"Server started and listening on {HOST}:{PORT}")
        print(f"Using a thread pool with a max of {MAX_WORKERS} workers.")

        # Create a thread pool executor
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            while True:
                # Accept a new connection - this is a blocking call
                conn, addr = server_socket.accept()
                # Submit the client handling task to the thread pool
                # The executor will run handle_client(conn, addr) in a separate thread
                executor.submit(handle_client, conn, addr)

if __name__ == "__main__":
    start_server()

