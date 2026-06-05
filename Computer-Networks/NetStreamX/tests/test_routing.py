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

from protocols.routing import Router

router = Router("Test-Router")

router.add_route(
    "Network-A",
    "Router-A"
)

router.route_packet(
    "Network-A"
)

print("\nRouting Test Passed")