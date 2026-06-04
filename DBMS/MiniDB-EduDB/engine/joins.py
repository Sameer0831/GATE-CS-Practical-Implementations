import json
import os


class JoinOperations:

    # -----------------------------------------
    # INNER JOIN
    # -----------------------------------------
    def inner_join(
        self,
        table1,
        table2,
        table1_column,
        table2_column
    ):

        table1_file = f"data/{table1}.json"
        table2_file = f"data/{table2}.json"

        # Table existence validation
        if not os.path.exists(table1_file):
            print(f"Table '{table1}' does not exist.")
            return

        if not os.path.exists(table2_file):
            print(f"Table '{table2}' does not exist.")
            return

        # Load data
        with open(table1_file, "r") as file:
            data1 = json.load(file)

        with open(table2_file, "r") as file:
            data2 = json.load(file)

        print("\n========== INNER JOIN RESULT ==========\n")

        joined = False

        # Nested Loop Join
        for row1 in data1:

            for row2 in data2:

                if str(row1.get(table1_column)) == str(
                    row2.get(table2_column)
                ):

                    merged_row = {**row1, **row2}

                    print(merged_row)

                    joined = True

        if not joined:
            print("No matching records found.")

    # -----------------------------------------
    # LEFT JOIN
    # -----------------------------------------
    def left_join(
        self,
        table1,
        table2,
        table1_column,
        table2_column
    ):

        table1_file = f"data/{table1}.json"
        table2_file = f"data/{table2}.json"

        if not os.path.exists(table1_file):
            print(f"Table '{table1}' does not exist.")
            return

        if not os.path.exists(table2_file):
            print(f"Table '{table2}' does not exist.")
            return

        with open(table1_file, "r") as file:
            data1 = json.load(file)

        with open(table2_file, "r") as file:
            data2 = json.load(file)

        print("\n========== LEFT JOIN RESULT ==========\n")

        for row1 in data1:

            matched = False

            for row2 in data2:

                if str(row1.get(table1_column)) == str(
                    row2.get(table2_column)
                ):

                    merged_row = {**row1, **row2}

                    print(merged_row)

                    matched = True

            if not matched:
                print(row1)

    # -----------------------------------------
    # RIGHT JOIN
    # -----------------------------------------
    def right_join(
        self,
        table1,
        table2,
        table1_column,
        table2_column
    ):

        table1_file = f"data/{table1}.json"
        table2_file = f"data/{table2}.json"

        if not os.path.exists(table1_file):
            print(f"Table '{table1}' does not exist.")
            return

        if not os.path.exists(table2_file):
            print(f"Table '{table2}' does not exist.")
            return

        with open(table1_file, "r") as file:
            data1 = json.load(file)

        with open(table2_file, "r") as file:
            data2 = json.load(file)

        print("\n========== RIGHT JOIN RESULT ==========\n")

        for row2 in data2:

            matched = False

            for row1 in data1:

                if str(row1.get(table1_column)) == str(
                    row2.get(table2_column)
                ):

                    merged_row = {**row1, **row2}

                    print(merged_row)

                    matched = True

            if not matched:
                print(row2)