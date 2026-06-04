import json
import os


class RelationalAlgebra:

    # -----------------------------------------
    # SELECTION OPERATION
    # -----------------------------------------
    def selection(
        self,
        table_name,
        column,
        value
    ):

        table_file = f"data/{table_name}.json"

        if not os.path.exists(table_file):

            print(f"Table '{table_name}' does not exist.")
            return

        with open(table_file, "r") as file:
            data = json.load(file)

        print(
            "\n========== SELECTION OPERATION ==========\n"
        )

        found = False

        for record in data:

            if str(record.get(column)) == str(value):

                print(record)
                found = True

        if not found:
            print("No matching records found.")

    # -----------------------------------------
    # PROJECTION OPERATION
    # -----------------------------------------
    def projection(
        self,
        table_name,
        columns
    ):

        table_file = f"data/{table_name}.json"

        if not os.path.exists(table_file):

            print(f"Table '{table_name}' does not exist.")
            return

        with open(table_file, "r") as file:
            data = json.load(file)

        print(
            "\n========== PROJECTION OPERATION ==========\n"
        )

        for record in data:

            projected_record = {}

            for column in columns:

                if column in record:
                    projected_record[column] = record[column]

            print(projected_record)

    # -----------------------------------------
    # UNION OPERATION
    # -----------------------------------------
    def union(
        self,
        table1,
        table2
    ):

        file1 = f"data/{table1}.json"
        file2 = f"data/{table2}.json"

        if not os.path.exists(file1):
            print(f"Table '{table1}' does not exist.")
            return

        if not os.path.exists(file2):
            print(f"Table '{table2}' does not exist.")
            return

        with open(file1, "r") as f1:
            data1 = json.load(f1)

        with open(file2, "r") as f2:
            data2 = json.load(f2)

        union_result = data1.copy()

        for record in data2:

            if record not in union_result:
                union_result.append(record)

        print(
            "\n========== UNION OPERATION ==========\n"
        )

        for record in union_result:
            print(record)

    # -----------------------------------------
    # INTERSECTION OPERATION
    # -----------------------------------------
    def intersection(
        self,
        table1,
        table2
    ):

        file1 = f"data/{table1}.json"
        file2 = f"data/{table2}.json"

        if not os.path.exists(file1):
            print(f"Table '{table1}' does not exist.")
            return

        if not os.path.exists(file2):
            print(f"Table '{table2}' does not exist.")
            return

        with open(file1, "r") as f1:
            data1 = json.load(f1)

        with open(file2, "r") as f2:
            data2 = json.load(f2)

        print(
            "\n========== INTERSECTION OPERATION ==========\n"
        )

        found = False

        for record in data1:

            if record in data2:

                print(record)
                found = True

        if not found:
            print("No common records found.")

    # -----------------------------------------
    # DIFFERENCE OPERATION
    # -----------------------------------------
    def difference(
        self,
        table1,
        table2
    ):

        file1 = f"data/{table1}.json"
        file2 = f"data/{table2}.json"

        if not os.path.exists(file1):
            print(f"Table '{table1}' does not exist.")
            return

        if not os.path.exists(file2):
            print(f"Table '{table2}' does not exist.")
            return

        with open(file1, "r") as f1:
            data1 = json.load(f1)

        with open(file2, "r") as f2:
            data2 = json.load(f2)

        print(
            "\n========== DIFFERENCE OPERATION ==========\n"
        )

        found = False

        for record in data1:

            if record not in data2:

                print(record)
                found = True

        if not found:
            print("No unique records found.")

    # -----------------------------------------
    # CARTESIAN PRODUCT
    # -----------------------------------------
    def cartesian_product(
        self,
        table1,
        table2
    ):

        file1 = f"data/{table1}.json"
        file2 = f"data/{table2}.json"

        if not os.path.exists(file1):
            print(f"Table '{table1}' does not exist.")
            return

        if not os.path.exists(file2):
            print(f"Table '{table2}' does not exist.")
            return

        with open(file1, "r") as f1:
            data1 = json.load(f1)

        with open(file2, "r") as f2:
            data2 = json.load(f2)

        print(
            "\n========== CARTESIAN PRODUCT ==========\n"
        )

        for row1 in data1:

            for row2 in data2:

                combined = {**row1, **row2}

                print(combined)

    # -----------------------------------------
    # RENAME OPERATION
    # -----------------------------------------
    def rename_table(
        self,
        old_name,
        new_name
    ):

        old_file = f"data/{old_name}.json"
        new_file = f"data/{new_name}.json"

        if not os.path.exists(old_file):

            print(f"Table '{old_name}' does not exist.")
            return

        os.rename(old_file, new_file)

        print(
            f"\nTable renamed from "
            f"'{old_name}' to '{new_name}'."
        )

    # -----------------------------------------
    # DIVISION OPERATION DEMO
    # -----------------------------------------
    def division_demo(self):

        print(
            "\n========== DIVISION OPERATION ==========\n"
        )

        print(
            "Division operation retrieves tuples "
            "associated with ALL values "
            "in another relation."
        )