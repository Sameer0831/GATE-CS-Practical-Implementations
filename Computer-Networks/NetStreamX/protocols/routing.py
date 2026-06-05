class Router:

    def __init__(self, name):

        self.name = name
        self.routes = {}

    def add_route(self, destination, next_hop):

        self.routes[destination] = next_hop

    def route_packet(self, destination):

        if destination in self.routes:

            print(
                f"{self.name} forwards packet to "
                f"{self.routes[destination]}"
            )

        else:

            print(
                f"{self.name}: No route found "
                f"for {destination}"
            )


router_a = Router("Router-A")

router_a.add_route(
    "Network-B",
    "Router-B"
)

router_a.add_route(
    "Network-C",
    "Router-C"
)

print("\nRouting Table")

for destination, next_hop in router_a.routes.items():

    print(
        f"{destination} -> {next_hop}"
    )

print("\nPacket Routing Simulation")

router_a.route_packet("Network-B")
router_a.route_packet("Network-C")
router_a.route_packet("Network-X")