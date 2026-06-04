import json
import os


class HashIndexer:

    def __init__(self):

        # In-memory indexes
        self.indexes = {}

    # -----------------------------------------
    # CREATE HASH INDEX
    # -----------------------------------------
    def create_index(self, table_name, column):

        table_file = f"data/{table_name}.json"

        # Table existence validation
        if not os.path.exists(table_file):
            print(f"Table '{table_name}' does not exist.")
            return

        with open(table_file, "r") as file:
            data = json.load(file)

        index = {}

        # Build hash index
        for record in data:

            key = record.get(column)

            if key not in index:
                index[key] = []

            index[key].append(record)

        # Store index in memory
        self.indexes[(table_name, column)] = index

        print(
            f"\nHash index created on "
            f"'{table_name}.{column}' successfully."
        )

    # -----------------------------------------
    # DISPLAY INDEX
    # -----------------------------------------
    def show_index(self, table_name, column):

        key = (table_name, column)

        if key not in self.indexes:

            print(
                f"No index found on "
                f"'{table_name}.{column}'."
            )

            return

        print(
            f"\n========== HASH INDEX "
            f"({table_name}.{column}) ==========\n"
        )

        index = self.indexes[key]

        for value, records in index.items():

            print(f"{value} -> {records}")

    # -----------------------------------------
    # INDEXED SEARCH
    # -----------------------------------------
    def search_using_index(
        self,
        table_name,
        column,
        value
    ):

        key = (table_name, column)

        if key not in self.indexes:

            print(
                f"No index found on "
                f"'{table_name}.{column}'."
            )

            return

        index = self.indexes[key]

        print(
            f"\n========== INDEX SEARCH RESULT ==========\n"
        )

        if value in index:

            for record in index[value]:
                print(record)

        else:
            print("No matching records found.")

    # -----------------------------------------
    # DELETE INDEX
    # -----------------------------------------
    def drop_index(self, table_name, column):

        key = (table_name, column)

        if key not in self.indexes:

            print(
                f"No index exists on "
                f"'{table_name}.{column}'."
            )

            return

        del self.indexes[key]

        print(
            f"Index on '{table_name}.{column}' "
            f"deleted successfully."
        )