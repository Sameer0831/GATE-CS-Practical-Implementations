import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from protocols.packet import Packet

packet = Packet(
    "192.168.1.1",
    "8.8.8.8",
    "TCP",
    "Test Packet"
)

packet.display()

print("\nPacket Test Passed")