class Packet:

    def __init__(
        self,
        source_ip,
        destination_ip,
        protocol,
        payload
    ):

        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.protocol = protocol
        self.payload = payload

    def display(self):

        print("\nPacket Information")
        print("-------------------")

        print(
            f"Source IP: "
            f"{self.source_ip}"
        )

        print(
            f"Destination IP: "
            f"{self.destination_ip}"
        )

        print(
            f"Protocol: "
            f"{self.protocol}"
        )

        print(
            f"Payload: "
            f"{self.payload}"
        )


packet = Packet(
    source_ip="192.168.1.10",
    destination_ip="8.8.8.8",
    protocol="TCP",
    payload="Hello Network"
)

packet.display()