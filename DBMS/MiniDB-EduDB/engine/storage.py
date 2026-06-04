import json
import os


class StorageEngine:

    def __init__(self):

        self.block_size = 4

    # -----------------------------------------
    # DISPLAY STORAGE ARCHITECTURE
    # -----------------------------------------
    def storage_architecture(self):

        print(
            "\n========== STORAGE ARCHITECTURE ==========\n"
        )

        print(
            "Disk Storage\n"
            "   ↓\n"
            "Files\n"
            "   ↓\n"
            "Blocks / Pages\n"
            "   ↓\n"
            "Records / Tuples"
        )

    # -----------------------------------------
    # SEQUENTIAL FILE ORGANIZATION
    # -----------------------------------------
    def sequential_storage(self, table_name):

        table_file = f"data/{table_name}.json"

        if not os.path.exists(table_file):

            print(f"Table '{table_name}' does not exist.")
            return

        with open(table_file, "r") as file:
            data = json.load(file)

        print(
            "\n========== SEQUENTIAL FILE ORGANIZATION ==========\n"
        )

        for index, record in enumerate(data):

            print(
                f"Record {index + 1}: {record}"
            )

    # -----------------------------------------
    # PAGE / BLOCK SIMULATION
    # -----------------------------------------
    def simulate_pages(self, table_name):

        table_file = f"data/{table_name}.json"

        if not os.path.exists(table_file):

            print(f"Table '{table_name}' does not exist.")
            return

        with open(table_file, "r") as file:
            data = json.load(file)

        print(
            "\n========== PAGE ORGANIZATION ==========\n"
        )

        page_number = 1

        for i in range(0, len(data), self.block_size):

            page = data[i:i + self.block_size]

            print(
                f"\nPAGE {page_number}\n"
            )

            for record in page:

                print(record)

            page_number += 1

    # -----------------------------------------
    # STORAGE BLOCK DEMO
    # -----------------------------------------
    def block_demo(self):

        print(
            "\n========== STORAGE BLOCKS ==========\n"
        )

        print(
            "Block 1 -> Records 1 to 4\n"
            "Block 2 -> Records 5 to 8\n"
            "Block 3 -> Records 9 to 12"
        )

    # -----------------------------------------
    # HEAP FILE ORGANIZATION
    # -----------------------------------------
    def heap_file_demo(self):

        print(
            "\n========== HEAP FILE ORGANIZATION ==========\n"
        )

        print(
            "Records stored in arbitrary order.\n"
            "Insertion is fast.\n"
            "Searching may require full scan."
        )

    # -----------------------------------------
    # HASH FILE ORGANIZATION
    # -----------------------------------------
    def hash_file_demo(self):

        print(
            "\n========== HASH FILE ORGANIZATION ==========\n"
        )

        print(
            "Hash function maps keys to buckets.\n"
            "Provides faster exact-match retrieval."
        )

    # -----------------------------------------
    # INDEXED FILE ORGANIZATION
    # -----------------------------------------
    def indexed_file_demo(self):

        print(
            "\n========== INDEXED FILE ORGANIZATION ==========\n"
        )

        print(
            "Indexes improve search performance.\n"
            "Additional storage required for indexes."
        )

    # -----------------------------------------
    # BUFFER MANAGER DEMO
    # -----------------------------------------
    def buffer_manager_demo(self):

        print(
            "\n========== BUFFER MANAGER ==========\n"
        )

        print(
            "Buffer Manager Responsibilities:\n"
            "- Load pages into memory\n"
            "- Reduce disk I/O\n"
            "- Replace pages using policies"
        )

    # -----------------------------------------
    # PAGE REPLACEMENT DEMO
    # -----------------------------------------
    def page_replacement_demo(self):

        print(
            "\n========== PAGE REPLACEMENT ==========\n"
        )

        print(
            "Popular Algorithms:\n"
            "- FIFO\n"
            "- LRU\n"
            "- Clock Algorithm"
        )

    # -----------------------------------------
    # DISK ACCESS COST DEMO
    # -----------------------------------------
    def disk_access_demo(self):

        print(
            "\n========== DISK ACCESS COST ==========\n"
        )

        print(
            "Disk access is expensive.\n"
            "Indexes and buffering reduce I/O cost."
        )

    # -----------------------------------------
    # FILE ORGANIZATION SUMMARY
    # -----------------------------------------
    def file_organization_summary(self):

        print(
            "\n========== FILE ORGANIZATION SUMMARY ==========\n"
        )

        print(
            "1. Sequential Organization\n"
            "2. Heap File Organization\n"
            "3. Hash File Organization\n"
            "4. Indexed File Organization"
        )