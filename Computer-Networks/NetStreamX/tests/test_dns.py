import socket

def test_dns():

    ip = socket.gethostbyname("google.com")

    print("DNS Test Passed")
    print(ip)

test_dns()