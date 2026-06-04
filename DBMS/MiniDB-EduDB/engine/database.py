import os
import json


class Database:

    def __init__(self):

        self.data_path = "data"

        # Create data directory if not exists
        if not os.path.exists(self.data_path):
            os.makedirs(self.data_path)

    # -----------------------------------------
    # CREATE TABLE
    # -----------------------------------------
    def create_table(self, table_name):

        table_file = f"{self.data_path}/{table_name}.json"

        # Prevent duplicate table creation
        if os.path.exists(table_file):
            print(f"Table '{table_name}' already exists.")
            return

        # Create empty relation
        with open(table_file, "w") as file:
            json.dump([], file)

        print(f"Table '{table_name}' created successfully.")

    # -----------------------------------------
    # INSERT RECORD
    # -----------------------------------------
    def insert_into(self, table_name, record):

        table_file = f"{self.data_path}/{table_name}.json"

        # Table existence validation
        if not os.path.exists(table_file):
            print(f"Table '{table_name}' does not exist.")
            return

        # Load current table data
        with open(table_file, "r") as file:
            data = json.load(file)

        # Insert tuple
        data.append(record)

        # Save updated table
        with open(table_file, "w") as file:
            json.dump(data, file, indent=4)

        print(f"Inserted record into '{table_name}'.")

    # -----------------------------------------
    # SELECT ALL RECORDS
    # -----------------------------------------
    def select_all(self, table_name):

        table_file = f"{self.data_path}/{table_name}.json"

        if not os.path.exists(table_file):
            print(f"Table '{table_name}' does not exist.")
            return

        with open(table_file, "r") as file:
            data = json.load(file)

        if not data:
            print("No records found.")
            return

        print(f"\n========== RECORDS FROM {table_name.upper()} ==========\n")

        for record in data:
            print(record)

    # -----------------------------------------
    # WHERE CONDITION
    # -----------------------------------------
    def select_where(self, table_name, column, value):

        table_file = f"{self.data_path}/{table_name}.json"

        if not os.path.exists(table_file):
            print(f"Table '{table_name}' does not exist.")
            return

        with open(table_file, "r") as file:
            data = json.load(file)

        print(f"\n========== FILTERED RECORDS ==========\n")

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
    def project_columns(self, table_name, columns):

        table_file = f"{self.data_path}/{table_name}.json"

        if not os.path.exists(table_file):
            print(f"Table '{table_name}' does not exist.")
            return

        with open(table_file, "r") as file:
            data = json.load(file)

        print(f"\n========== PROJECTED COLUMNS ==========\n")

        for record in data:

            projected_record = {}

            for column in columns:

                if column in record:
                    projected_record[column] = record[column]

            print(projected_record)

    # -----------------------------------------
    # UPDATE RECORDS
    # -----------------------------------------
    def update_records(
        self,
        table_name,
        condition_column,
        condition_value,
        update_column,
        new_value
    ):

        table_file = f"{self.data_path}/{table_name}.json"

        if not os.path.exists(table_file):
            print(f"Table '{table_name}' does not exist.")
            return

        with open(table_file, "r") as file:
            data = json.load(file)

        updated = False

        for record in data:

            if str(record.get(condition_column)) == str(condition_value):

                record[update_column] = new_value
                updated = True

        with open(table_file, "w") as file:
            json.dump(data, file, indent=4)

        if updated:
            print("Records updated successfully.")
        else:
            print("No matching records found.")

    # -----------------------------------------
    # DELETE RECORDS
    # -----------------------------------------
    def delete_records(self, table_name, column, value):

        table_file = f"{self.data_path}/{table_name}.json"

        if not os.path.exists(table_file):
            print(f"Table '{table_name}' does not exist.")
            return

        with open(table_file, "r") as file:
            data = json.load(file)

        new_data = []

        deleted = False

        for record in data:

            if str(record.get(column)) != str(value):
                new_data.append(record)
            else:
                deleted = True

        with open(table_file, "w") as file:
            json.dump(new_data, file, indent=4)

        if deleted:
            print("Matching records deleted.")
        else:
            print("No matching records found.")

    # -----------------------------------------
    # COUNT RECORDS
    # -----------------------------------------
    def count_records(self, table_name):

        table_file = f"{self.data_path}/{table_name}.json"

        if not os.path.exists(table_file):
            print(f"Table '{table_name}' does not exist.")
            return

        with open(table_file, "r") as file:
            data = json.load(file)

        print(f"\nTotal Records: {len(data)}")

    # -----------------------------------------
    # SHOW TABLES
    # -----------------------------------------
    def show_tables(self):

        tables = os.listdir(self.data_path)

        if not tables:
            print("No tables found.")
            return

        print("\n========== TABLES ==========\n")

        for table in tables:
            print(table.replace(".json", ""))

    # -----------------------------------------
    # DROP TABLE
    # -----------------------------------------
    def drop_table(self, table_name):

        table_file = f"{self.data_path}/{table_name}.json"

        if not os.path.exists(table_file):
            print(f"Table '{table_name}' does not exist.")
            return

        os.remove(table_file)

        print(f"Table '{table_name}' deleted successfully.")