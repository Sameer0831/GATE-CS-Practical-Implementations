class ConcurrencyController:

    def __init__(self):

        # Lock table
        self.locks = {}

    # -----------------------------------------
    # SHARED LOCK
    # -----------------------------------------
    def shared_lock(self, transaction_id, item):

        # Check existing lock
        if item in self.locks:

            existing_lock = self.locks[item]

            # Exclusive lock conflict
            if existing_lock["type"] == "X":

                print(
                    f"\nSHARED LOCK DENIED:\n"
                    f"{item} already has an Exclusive Lock."
                )

                return

            # Add shared transaction
            existing_lock["transactions"].append(transaction_id)

        else:

            self.locks[item] = {
                "type": "S",
                "transactions": [transaction_id]
            }

        print(
            f"\nShared Lock granted:\n"
            f"Transaction {transaction_id} -> {item}"
        )

    # -----------------------------------------
    # EXCLUSIVE LOCK
    # -----------------------------------------
    def exclusive_lock(self, transaction_id, item):

        # Check existing lock
        if item in self.locks:

            print(
                f"\nEXCLUSIVE LOCK DENIED:\n"
                f"{item} already locked."
            )

            return

        self.locks[item] = {
            "type": "X",
            "transactions": [transaction_id]
        }

        print(
            f"\nExclusive Lock granted:\n"
            f"Transaction {transaction_id} -> {item}"
        )

    # -----------------------------------------
    # RELEASE LOCK
    # -----------------------------------------
    def release_lock(self, transaction_id, item):

        if item not in self.locks:

            print(f"\nNo lock found on {item}.")
            return

        lock_info = self.locks[item]

        if transaction_id not in lock_info["transactions"]:

            print(
                f"\nTransaction {transaction_id} "
                f"does not hold lock on {item}."
            )

            return

        # Remove transaction from lock
        lock_info["transactions"].remove(transaction_id)

        # Remove entire lock if no transactions remain
        if len(lock_info["transactions"]) == 0:

            del self.locks[item]

        print(
            f"\nLock released:\n"
            f"Transaction {transaction_id} -> {item}"
        )

    # -----------------------------------------
    # DISPLAY LOCK TABLE
    # -----------------------------------------
    def show_locks(self):

        print("\n========== LOCK TABLE ==========\n")

        if not self.locks:

            print("No active locks.")
            return

        for item, lock_info in self.locks.items():

            print(
                f"{item} -> "
                f"Type: {lock_info['type']} | "
                f"Transactions: {lock_info['transactions']}"
            )

    # -----------------------------------------
    # TWO PHASE LOCKING SIMULATION
    # -----------------------------------------
    def two_phase_locking_demo(self):

        print(
            "\n========== TWO PHASE LOCKING ==========\n"
        )

        print("Growing Phase:")
        print("Transaction acquires locks.")

        print("\nShrinking Phase:")
        print("Transaction releases locks.")

        print(
            "\n2PL ensures conflict serializability."
        )