import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input("Enter host ip address or hostname:\n")  # Listen on all available interfaces
    port = int(input("Enter port:\n"))  # Choose a port number

    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Received: {data}")

        response = input("Enter response: ")
        conn.send(response.encode())

    conn.close()

if __name__ == "__main__":
    start_server()