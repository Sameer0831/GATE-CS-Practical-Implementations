import socket

print("DNS Lookup Tool")
print("----------------")

while True:

    domain = input("\nEnter domain (or 'exit'): ")

    if domain.lower() == "exit":
        break

    try:

        ip = socket.gethostbyname(domain)

        print(f"IP Address: {ip}")

    except Exception as e:

        print("Lookup failed")
        print(e)