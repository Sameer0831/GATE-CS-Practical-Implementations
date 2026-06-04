import json
import os
from datetime import datetime


class TransactionManager:

    def __init__(self):

        self.log_file = "data/transaction_log.json"

        # Create transaction log if not exists
        if not os.path.exists(self.log_file):

            with open(self.log_file, "w") as file:
                json.dump([], file)

    # -----------------------------------------
    # WRITE LOG ENTRY
    # -----------------------------------------
    def write_log(self, transaction_id, operation, status):

        with open(self.log_file, "r") as file:
            logs = json.load(file)

        log_entry = {

            "transaction_id": transaction_id,
            "operation": operation,
            "status": status,
            "timestamp": str(datetime.now())
        }

        logs.append(log_entry)

        with open(self.log_file, "w") as file:
            json.dump(logs, file, indent=4)

    # -----------------------------------------
    # BEGIN TRANSACTION
    # -----------------------------------------
    def begin_transaction(self, transaction_id):

        print(
            f"\nTransaction '{transaction_id}' started."
        )

        self.write_log(
            transaction_id,
            "BEGIN TRANSACTION",
            "STARTED"
        )

    # -----------------------------------------
    # COMMIT TRANSACTION
    # -----------------------------------------
    def commit_transaction(self, transaction_id):

        print(
            f"Transaction '{transaction_id}' committed."
        )

        self.write_log(
            transaction_id,
            "COMMIT",
            "SUCCESS"
        )

    # -----------------------------------------
    # ROLLBACK TRANSACTION
    # -----------------------------------------
    def rollback_transaction(self, transaction_id):

        print(
            f"Transaction '{transaction_id}' rolled back."
        )

        self.write_log(
            transaction_id,
            "ROLLBACK",
            "REVERTED"
        )

    # -----------------------------------------
    # DISPLAY TRANSACTION LOGS
    # -----------------------------------------
    def show_logs(self):

        with open(self.log_file, "r") as file:
            logs = json.load(file)

        print(
            "\n========== TRANSACTION LOGS ==========\n"
        )

        for log in logs:

            print(log)

    # -----------------------------------------
    # CLEAR LOGS
    # -----------------------------------------
    def clear_logs(self):

        with open(self.log_file, "w") as file:
            json.dump([], file)

        print("Transaction logs cleared.")