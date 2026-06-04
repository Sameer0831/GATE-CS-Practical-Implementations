from engine.database import Database
from engine.parser import SQLParser


class QueryExecutor:

    def __init__(self):

        self.db = Database()
        self.parser = SQLParser()

    # -----------------------------------------
    # EXECUTE QUERY
    # -----------------------------------------
    def execute(self, query):

        parsed_query = self.parser.parse(query)

        if not parsed_query:
            return

        command = parsed_query["command"]
        tokens = parsed_query["tokens"]

        print(
            "\n========== QUERY EXECUTOR ==========\n"
        )

        # -----------------------------------------
        # CREATE TABLE
        # -----------------------------------------
        if command == "CREATE":

            if len(tokens) < 3:

                print("Invalid CREATE query.")
                return

            table_name = tokens[2]

            self.db.create_table(table_name)

        # -----------------------------------------
        # SELECT
        # -----------------------------------------
        elif command == "SELECT":

            if len(tokens) < 4:

                print("Invalid SELECT query.")
                return

            table_name = tokens[3]

            self.db.select_all(table_name)

        # -----------------------------------------
        # INSERT
        # -----------------------------------------
        elif command == "INSERT":

            print(
                "INSERT parsing demo completed."
            )

        # -----------------------------------------
        # UPDATE
        # -----------------------------------------
        elif command == "UPDATE":

            print(
                "UPDATE parsing demo completed."
            )

        # -----------------------------------------
        # DELETE
        # -----------------------------------------
        elif command == "DELETE":

            print(
                "DELETE parsing demo completed."
            )

        # -----------------------------------------
        # DROP
        # -----------------------------------------
        elif command == "DROP":

            if len(tokens) < 3:

                print("Invalid DROP query.")
                return

            table_name = tokens[2]

            self.db.drop_table(table_name)

        # -----------------------------------------
        # UNKNOWN COMMAND
        # -----------------------------------------
        else:

            print(
                f"Unsupported SQL command: {command}"
            )

    # -----------------------------------------
    # QUERY EXECUTION DEMO
    # -----------------------------------------
    def execution_demo(self):

        print(
            "\n========== QUERY EXECUTION DEMO ==========\n"
        )

        sample_queries = [

            "CREATE TABLE employees",

            "SELECT * FROM students",

            "DROP TABLE employees"
        ]

        for query in sample_queries:

            print(f"\nExecuting Query:\n{query}")

            self.execute(query)

    # -----------------------------------------
    # QUERY PLAN DEMO
    # -----------------------------------------
    def query_plan_demo(self):

        print(
            "\n========== QUERY PLAN ==========\n"
        )

        print(
            "1. Parse Query\n"
            "2. Validate Query\n"
            "3. Generate Execution Plan\n"
            "4. Access Storage Engine\n"
            "5. Execute Operation\n"
            "6. Return Result"
        )

    # -----------------------------------------
    # OPTIMIZATION DEMO
    # -----------------------------------------
    def optimization_demo(self):

        print(
            "\n========== QUERY OPTIMIZATION ==========\n"
        )

        print(
            "Optimization Techniques:\n"
            "- Predicate Pushdown\n"
            "- Index Utilization\n"
            "- Join Optimization\n"
            "- Projection Pushdown"
        )

    # -----------------------------------------
    # COST ESTIMATION DEMO
    # -----------------------------------------
    def cost_estimation_demo(self):

        print(
            "\n========== COST ESTIMATION ==========\n"
        )

        print(
            "Estimated Query Cost:\n"
            "- Full Table Scan: High Cost\n"
            "- Indexed Search: Low Cost\n"
            "- Nested Loop Join: Medium Cost"
        )