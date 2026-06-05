import socket

HOST = "127.0.0.1"
PORT = 8888

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

server.bind((HOST, PORT))

print(f"UDP Server listening on {HOST}:{PORT}")

while True:

    data, address = server.recvfrom(1024)

    message = data.decode()

    print(f"Client {address}: {message}")

    response = f"Received: {message}"

    server.sendto(
        response.encode(),
        address
    )