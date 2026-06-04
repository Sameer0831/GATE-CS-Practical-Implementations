import json
import os


class AggregationOperations:

    # -----------------------------------------
    # COUNT
    # -----------------------------------------
    def count(self, table_name):

        table_file = f"data/{table_name}.json"

        if not os.path.exists(table_file):
            print(f"Table '{table_name}' does not exist.")
            return

        with open(table_file, "r") as file:
            data = json.load(file)

        print(f"\nCOUNT = {len(data)}")

    # -----------------------------------------
    # SUM
    # -----------------------------------------
    def sum(self, table_name, column):

        table_file = f"data/{table_name}.json"

        if not os.path.exists(table_file):
            print(f"Table '{table_name}' does not exist.")
            return

        with open(table_file, "r") as file:
            data = json.load(file)

        total = 0

        for record in data:

            value = record.get(column)

            if isinstance(value, (int, float)):
                total += value

        print(f"\nSUM({column}) = {total}")

    # -----------------------------------------
    # AVG
    # -----------------------------------------
    def average(self, table_name, column):

        table_file = f"data/{table_name}.json"

        if not os.path.exists(table_file):
            print(f"Table '{table_name}' does not exist.")
            return

        with open(table_file, "r") as file:
            data = json.load(file)

        total = 0
        count = 0

        for record in data:

            value = record.get(column)

            if isinstance(value, (int, float)):
                total += value
                count += 1

        if count == 0:
            print("No numeric values found.")
            return

        avg = total / count

        print(f"\nAVG({column}) = {avg}")

    # -----------------------------------------
    # MIN
    # -----------------------------------------
    def minimum(self, table_name, column):

        table_file = f"data/{table_name}.json"

        if not os.path.exists(table_file):
            print(f"Table '{table_name}' does not exist.")
            return

        with open(table_file, "r") as file:
            data = json.load(file)

        values = []

        for record in data:

            value = record.get(column)

            if isinstance(value, (int, float)):
                values.append(value)

        if not values:
            print("No numeric values found.")
            return

        print(f"\nMIN({column}) = {min(values)}")

    # -----------------------------------------
    # MAX
    # -----------------------------------------
    def maximum(self, table_name, column):

        table_file = f"data/{table_name}.json"

        if not os.path.exists(table_file):
            print(f"Table '{table_name}' does not exist.")
            return

        with open(table_file, "r") as file:
            data = json.load(file)

        values = []

        for record in data:

            value = record.get(column)

            if isinstance(value, (int, float)):
                values.append(value)

        if not values:
            print("No numeric values found.")
            return

        print(f"\nMAX({column}) = {max(values)}")

    # -----------------------------------------
    # GROUP BY COUNT
    # -----------------------------------------
    def group_by_count(self, table_name, column):

        table_file = f"data/{table_name}.json"

        if not os.path.exists(table_file):
            print(f"Table '{table_name}' does not exist.")
            return

        with open(table_file, "r") as file:
            data = json.load(file)

        group_counts = {}

        for record in data:

            key = record.get(column)

            if key not in group_counts:
                group_counts[key] = 0

            group_counts[key] += 1

        print(f"\n========== GROUP BY {column.upper()} ==========\n")

        for key, count in group_counts.items():

            print(f"{key} : {count}")

    # -----------------------------------------
    # GROUP BY AVG
    # -----------------------------------------
    def group_by_average(
        self,
        table_name,
        group_column,
        value_column
    ):

        table_file = f"data/{table_name}.json"

        if not os.path.exists(table_file):
            print(f"Table '{table_name}' does not exist.")
            return

        with open(table_file, "r") as file:
            data = json.load(file)

        groups = {}

        for record in data:

            group_key = record.get(group_column)
            value = record.get(value_column)

            if isinstance(value, (int, float)):

                if group_key not in groups:
                    groups[group_key] = []

                groups[group_key].append(value)

        print(
            f"\n========== GROUP BY {group_column.upper()} "
            f"AVG({value_column.upper()}) ==========\n"
        )

        for key, values in groups.items():

            avg = sum(values) / len(values)

            print(f"{key} : {avg}")