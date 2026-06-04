import json
import os


class ConstraintManager:

    # -----------------------------------------
    # PRIMARY KEY VALIDATION
    # -----------------------------------------
    def check_primary_key(
        self,
        table_name,
        primary_key_column,
        value
    ):

        table_file = f"data/{table_name}.json"

        # Table existence check
        if not os.path.exists(table_file):
            print(f"Table '{table_name}' does not exist.")
            return False

        with open(table_file, "r") as file:
            data = json.load(file)

        # Duplicate primary key check
        for record in data:

            if str(record.get(primary_key_column)) == str(value):

                print(
                    f"PRIMARY KEY CONSTRAINT VIOLATION:\n"
                    f"Duplicate value '{value}' "
                    f"found in column '{primary_key_column}'."
                )

                return False

        return True

    # -----------------------------------------
    # FOREIGN KEY VALIDATION
    # -----------------------------------------
    def check_foreign_key(
        self,
        parent_table,
        parent_column,
        value
    ):

        parent_file = f"data/{parent_table}.json"

        # Parent table existence
        if not os.path.exists(parent_file):
            print(f"Parent table '{parent_table}' does not exist.")
            return False

        with open(parent_file, "r") as file:
            data = json.load(file)

        # Foreign key reference validation
        for record in data:

            if str(record.get(parent_column)) == str(value):
                return True

        print(
            f"FOREIGN KEY CONSTRAINT VIOLATION:\n"
            f"Value '{value}' not found in "
            f"'{parent_table}.{parent_column}'."
        )

        return False

    # -----------------------------------------
    # UNIQUE CONSTRAINT
    # -----------------------------------------
    def check_unique_constraint(
        self,
        table_name,
        column,
        value
    ):

        table_file = f"data/{table_name}.json"

        if not os.path.exists(table_file):
            print(f"Table '{table_name}' does not exist.")
            return False

        with open(table_file, "r") as file:
            data = json.load(file)

        for record in data:

            if str(record.get(column)) == str(value):

                print(
                    f"UNIQUE CONSTRAINT VIOLATION:\n"
                    f"Duplicate value '{value}' "
                    f"found in column '{column}'."
                )

                return False

        return True

    # -----------------------------------------
    # NOT NULL CONSTRAINT
    # -----------------------------------------
    def check_not_null(self, column_name, value):

        if value is None or value == "":

            print(
                f"NOT NULL CONSTRAINT VIOLATION:\n"
                f"Column '{column_name}' cannot be NULL."
            )

            return False

        return True

    # -----------------------------------------
    # DOMAIN CONSTRAINT
    # -----------------------------------------
    def check_marks_domain(self, marks):

        if marks < 0 or marks > 100:

            print(
                "DOMAIN CONSTRAINT VIOLATION:\n"
                "Marks should be between 0 and 100."
            )

            return False

        return True