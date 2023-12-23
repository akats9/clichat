import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'  # Change to the server's IP address
    port = int(input("Enter port:"))  # Use the same port number as the server

    client_socket.connect((host, port))

    while True:
        message = input("Enter message: ")
        client_socket.send(message.encode())

        response = client_socket.recv(1024).decode()
        print(f"Received response: {response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
