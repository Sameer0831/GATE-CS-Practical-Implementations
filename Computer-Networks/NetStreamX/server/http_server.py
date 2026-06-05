import socket

HOST = "127.0.0.1"
PORT = 8080

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind((HOST, PORT))
server.listen()

print(f"HTTP Server running at http://{HOST}:{PORT}")

while True:

    client, address = server.accept()

    request = client.recv(1024).decode()

    print("\nREQUEST RECEIVED:")
    print(request)

    html = """
    <html>
        <head>
            <title>NetStreamX</title>
        </head>
        <body>
            <h1>Welcome to NetStreamX</h1>
            <p>Mini HTTP Server Built in Python</p>
        </body>
    </html>
    """

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n\r\n"
        + html
    )

    client.send(response.encode())

    client.close()