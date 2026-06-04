import json
import os
from datetime import datetime


class RecoveryManager:

    def __init__(self):

        self.recovery_log_file = "data/recovery_log.json"

        # Create recovery log file if not exists
        if not os.path.exists(self.recovery_log_file):

            with open(self.recovery_log_file, "w") as file:
                json.dump([], file)

    # -----------------------------------------
    # WRITE-AHEAD LOGGING (WAL)
    # -----------------------------------------
    def write_log(
        self,
        transaction_id,
        operation,
        table_name,
        old_value,
        new_value
    ):

        with open(self.recovery_log_file, "r") as file:
            logs = json.load(file)

        log_entry = {

            "transaction_id": transaction_id,
            "operation": operation,
            "table": table_name,
            "old_value": old_value,
            "new_value": new_value,
            "timestamp": str(datetime.now())
        }

        logs.append(log_entry)

        with open(self.recovery_log_file, "w") as file:
            json.dump(logs, file, indent=4)

        print(
            f"Recovery log written for "
            f"Transaction {transaction_id}"
        )

    # -----------------------------------------
    # DISPLAY RECOVERY LOGS
    # -----------------------------------------
    def show_logs(self):

        with open(self.recovery_log_file, "r") as file:
            logs = json.load(file)

        print(
            "\n========== RECOVERY LOGS ==========\n"
        )

        if not logs:

            print("No recovery logs found.")
            return

        for log in logs:

            print(log)

    # -----------------------------------------
    # UNDO OPERATION
    # -----------------------------------------
    def undo(self, transaction_id):

        with open(self.recovery_log_file, "r") as file:
            logs = json.load(file)

        print(
            f"\n========== UNDO OPERATION "
            f"FOR {transaction_id} ==========\n"
        )

        found = False

        # Reverse scan
        for log in reversed(logs):

            if log["transaction_id"] == transaction_id:

                print(
                    f"UNDO -> "
                    f"{log['operation']} | "
                    f"Table: {log['table']} | "
                    f"Restore: {log['old_value']}"
                )

                found = True

        if not found:

            print(
                f"No logs found for "
                f"Transaction {transaction_id}"
            )

    # -----------------------------------------
    # REDO OPERATION
    # -----------------------------------------
    def redo(self, transaction_id):

        with open(self.recovery_log_file, "r") as file:
            logs = json.load(file)

        print(
            f"\n========== REDO OPERATION "
            f"FOR {transaction_id} ==========\n"
        )

        found = False

        for log in logs:

            if log["transaction_id"] == transaction_id:

                print(
                    f"REDO -> "
                    f"{log['operation']} | "
                    f"Table: {log['table']} | "
                    f"Apply: {log['new_value']}"
                )

                found = True

        if not found:

            print(
                f"No logs found for "
                f"Transaction {transaction_id}"
            )

    # -----------------------------------------
    # CRASH RECOVERY SIMULATION
    # -----------------------------------------
    def simulate_crash(self):

        print(
            "\n========== SYSTEM CRASH ==========\n"
        )

        print(
            "System failure detected.\n"
            "Database recovering using logs..."
        )

    # -----------------------------------------
    # RECOVERY PROCESS
    # -----------------------------------------
    def recover_system(self):

        print(
            "\n========== RECOVERY PROCESS ==========\n"
        )

        print(
            "1. Reading recovery logs\n"
            "2. Performing REDO operations\n"
            "3. Performing UNDO operations\n"
            "4. Database recovered successfully"
        )

    # -----------------------------------------
    # CLEAR LOGS
    # -----------------------------------------
    def clear_logs(self):

        with open(self.recovery_log_file, "w") as file:
            json.dump([], file)

        print("Recovery logs cleared.")