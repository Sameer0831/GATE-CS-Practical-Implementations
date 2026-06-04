class SerializabilityChecker:

    def __init__(self):

        # Precedence graph
        self.graph = {}

    # -----------------------------------------
    # ADD EDGE TO GRAPH
    # -----------------------------------------
    def add_edge(self, from_transaction, to_transaction):

        if from_transaction not in self.graph:
            self.graph[from_transaction] = []

        self.graph[from_transaction].append(to_transaction)

    # -----------------------------------------
    # BUILD PRECEDENCE GRAPH
    # -----------------------------------------
    def build_precedence_graph(self, schedule):

        """
        Schedule Format Example:

        [
            ("T1", "WRITE", "A"),
            ("T2", "READ", "A"),
            ("T2", "WRITE", "B"),
            ("T3", "READ", "B")
        ]
        """

        self.graph = {}

        n = len(schedule)

        for i in range(n):

            t1, op1, item1 = schedule[i]

            for j in range(i + 1, n):

                t2, op2, item2 = schedule[j]

                # Ignore same transaction
                if t1 == t2:
                    continue

                # Conflict condition
                if item1 == item2:

                    if (
                        op1 == "WRITE"
                        or op2 == "WRITE"
                    ):

                        self.add_edge(t1, t2)

    # -----------------------------------------
    # DISPLAY PRECEDENCE GRAPH
    # -----------------------------------------
    def show_graph(self):

        print(
            "\n========== PRECEDENCE GRAPH ==========\n"
        )

        if not self.graph:

            print("Graph is empty.")
            return

        for transaction, neighbors in self.graph.items():

            print(
                f"{transaction} -> {neighbors}"
            )

    # -----------------------------------------
    # DFS FOR CYCLE DETECTION
    # -----------------------------------------
    def dfs_cycle_check(
        self,
        node,
        visited,
        recursion_stack
    ):

        visited.add(node)
        recursion_stack.add(node)

        neighbors = self.graph.get(node, [])

        for neighbor in neighbors:

            if neighbor not in visited:

                if self.dfs_cycle_check(
                    neighbor,
                    visited,
                    recursion_stack
                ):
                    return True

            elif neighbor in recursion_stack:
                return True

        recursion_stack.remove(node)

        return False

    # -----------------------------------------
    # CHECK SERIALIZABILITY
    # -----------------------------------------
    def check_conflict_serializable(self):

        visited = set()

        recursion_stack = set()

        for node in self.graph:

            if node not in visited:

                if self.dfs_cycle_check(
                    node,
                    visited,
                    recursion_stack
                ):

                    print(
                        "\nSchedule is NOT "
                        "Conflict Serializable."
                    )

                    return

        print(
            "\nSchedule IS "
            "Conflict Serializable."
        )

    # -----------------------------------------
    # DISPLAY SAMPLE SCHEDULE
    # -----------------------------------------
    def sample_schedule_demo(self):

        print(
            "\n========== SAMPLE SCHEDULE ==========\n"
        )

        schedule = [

            ("T1", "WRITE", "A"),
            ("T2", "READ", "A"),
            ("T2", "WRITE", "B"),
            ("T3", "READ", "B")
        ]

        for operation in schedule:

            print(operation)

        self.build_precedence_graph(schedule)

        self.show_graph()

        self.check_conflict_serializable()