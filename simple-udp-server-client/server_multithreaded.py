import socket
import threading
from concurrent.futures import ThreadPoolExecutor

HOST = '127.0.0.1'
PORT = 65432
MAX_WORKERS = 5

def handle_request(server_socket, data, addr):
    """
    This function is executed by a thread in the pool.
    It handles the processing of a single datagram.
    """
    print(f"Handling request from {addr} on thread {threading.get_ident()}")
    
    data_decoded = data.decode('utf-8')
    print(f"Received from {addr}: {data_decoded}")

    response = f"Server echoes: {data_decoded}"
    
    server_socket.sendto(response.encode('utf-8'), addr)


def start_server():
    """
    Starts the UDP server, listens for incoming datagrams,
    and submits each request to the thread pool for processing.
    """
    # Create a server socket using IPv4 and UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        # Bind the socket to the host and port
        server_socket.bind((HOST, PORT))
        print(f"UDP Server started and listening on {HOST}:{PORT}")

        # Create a thread pool executor
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            while True:
                # Wait for and receive a datagram from any client
                # This is a blocking call
                data, addr = server_socket.recvfrom(1024)
                
                # Submit the handling of this datagram to the thread pool
                executor.submit(handle_request, server_socket, data, addr)

if __name__ == "__main__":
    start_server()

