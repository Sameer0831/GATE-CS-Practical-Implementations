import socket

HOST = "127.0.0.1"
PORT = 8888

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

while True:

    message = input("Message: ")

    client.sendto(
        message.encode(),
        (HOST, PORT)
    )

    response, _ = client.recvfrom(1024)

    print(response.decode())