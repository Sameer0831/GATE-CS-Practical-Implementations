class SQLParser:

    # -----------------------------------------
    # PARSE QUERY
    # -----------------------------------------
    def parse(self, query):

        tokens = query.strip().split()

        if not tokens:

            print("Empty query.")
            return None

        command = tokens[0].upper()

        print(
            f"\n========== QUERY PARSER ==========\n"
        )

        print(f"Raw Query: {query}")

        print(f"\nParsed Tokens:")

        for token in tokens:

            print(token)

        print(f"\nDetected Command: {command}")

        return {

            "command": command,
            "tokens": tokens
        }

    # -----------------------------------------
    # PARSE SELECT QUERY
    # -----------------------------------------
    def parse_select(self, query):

        tokens = query.strip().split()

        print(
            "\n========== SELECT QUERY PARSER ==========\n"
        )

        print(tokens)

        return tokens

    # -----------------------------------------
    # PARSE INSERT QUERY
    # -----------------------------------------
    def parse_insert(self, query):

        tokens = query.strip().split()

        print(
            "\n========== INSERT QUERY PARSER ==========\n"
        )

        print(tokens)

        return tokens

    # -----------------------------------------
    # PARSE UPDATE QUERY
    # -----------------------------------------
    def parse_update(self, query):

        tokens = query.strip().split()

        print(
            "\n========== UPDATE QUERY PARSER ==========\n"
        )

        print(tokens)

        return tokens

    # -----------------------------------------
    # PARSE DELETE QUERY
    # -----------------------------------------
    def parse_delete(self, query):

        tokens = query.strip().split()

        print(
            "\n========== DELETE QUERY PARSER ==========\n"
        )

        print(tokens)

        return tokens

    # -----------------------------------------
    # SQL TOKENIZATION DEMO
    # -----------------------------------------
    def tokenization_demo(self):

        print(
            "\n========== SQL TOKENIZATION ==========\n"
        )

        query = (
            "SELECT name FROM students "
            "WHERE department = CSE"
        )

        print(f"Query:\n{query}")

        tokens = query.split()

        print("\nTokens:")

        for token in tokens:

            print(token)

    # -----------------------------------------
    # SIMPLE SQL VALIDATION
    # -----------------------------------------
    def validate_query(self, query):

        keywords = [

            "SELECT",
            "INSERT",
            "UPDATE",
            "DELETE",
            "CREATE",
            "DROP"
        ]

        tokens = query.strip().split()

        if not tokens:

            print("Invalid Query.")
            return False

        command = tokens[0].upper()

        if command not in keywords:

            print(
                f"Invalid SQL command: {command}"
            )

            return False

        print("Query validation successful.")

        return True