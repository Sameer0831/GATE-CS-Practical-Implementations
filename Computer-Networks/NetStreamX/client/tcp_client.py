import socket
import threading

HOST = "127.0.0.1"
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

name = input("Enter Name: ")

def receive_messages():

    while True:

        try:
            message = client.recv(1024)

            print(message.decode())

        except:
            break

def send_messages():

    while True:

        message = input()

        final_message = f"{name}: {message}"

        client.send(final_message.encode())

receive_thread = threading.Thread(
    target=receive_messages
)

send_thread = threading.Thread(
    target=send_messages
)

receive_thread.start()
send_thread.start()