import os

from engine.database import Database
from engine.constraints import ConstraintManager
from engine.joins import JoinOperations
from engine.aggregation import AggregationOperations
from engine.indexer import HashIndexer
from engine.transaction import TransactionManager
from engine.concurrency import ConcurrencyController
from engine.serializability import SerializabilityChecker
from engine.recovery import RecoveryManager
from engine.normalizer import Normalizer
from engine.er_model import ERModel
from engine.relational_algebra import RelationalAlgebra
from engine.parser import SQLParser
from engine.executor import QueryExecutor
from engine.storage import StorageEngine


# -------------------------------------------------
# CLEAN OLD FILES
# -------------------------------------------------

if os.path.exists("data/students.json"):
    os.remove("data/students.json")

if os.path.exists("data/departments.json"):
    os.remove("data/departments.json")


print("\n=================================================")
print("        EduDB - Educational DBMS Engine")
print("=================================================\n")


# -------------------------------------------------
# INITIALIZE MODULES
# -------------------------------------------------

db = Database()

constraints = ConstraintManager()

joins = JoinOperations()

aggregation = AggregationOperations()

indexer = HashIndexer()

transaction = TransactionManager()

concurrency = ConcurrencyController()

serial_checker = SerializabilityChecker()

recovery = RecoveryManager()

normalizer = Normalizer()

er = ERModel()

relational = RelationalAlgebra()

parser = SQLParser()

executor = QueryExecutor()

storage = StorageEngine()


# -------------------------------------------------
# CREATE TABLES
# -------------------------------------------------

print("\n================ CREATE TABLES ================\n")

db.create_table("students")

db.create_table("departments")


# -------------------------------------------------
# STUDENT DATASET
# -------------------------------------------------

students = [

    {"id": 1, "name": "Rajesh", "department": "CSE", "marks": 89},
    {"id": 2, "name": "Sameer", "department": "ECE", "marks": 76},
    {"id": 3, "name": "Akhil", "department": "MECH", "marks": 81},
    {"id": 4, "name": "Priya", "department": "CSE", "marks": 92},
    {"id": 5, "name": "Rohit", "department": "EEE", "marks": 68},
    {"id": 6, "name": "Sneha", "department": "CIVIL", "marks": 85},
    {"id": 7, "name": "Kiran", "department": "CSE", "marks": 74},
    {"id": 8, "name": "Neha", "department": "ECE", "marks": 90},
    {"id": 9, "name": "Arjun", "department": "MECH", "marks": 79},
    {"id": 10, "name": "Divya", "department": "CSE", "marks": 95},

    {"id": 11, "name": "Harsha", "department": "EEE", "marks": 72},
    {"id": 12, "name": "Pooja", "department": "CSE", "marks": 88},
    {"id": 13, "name": "Vamsi", "department": "ECE", "marks": 91},
    {"id": 14, "name": "Keerthi", "department": "CIVIL", "marks": 67},
    {"id": 15, "name": "Nikhil", "department": "MECH", "marks": 83},
    {"id": 16, "name": "Ananya", "department": "CSE", "marks": 94},
    {"id": 17, "name": "Teja", "department": "EEE", "marks": 78},
    {"id": 18, "name": "Meghana", "department": "ECE", "marks": 86},
    {"id": 19, "name": "Sandeep", "department": "MECH", "marks": 71},
    {"id": 20, "name": "Lavanya", "department": "CSE", "marks": 97},

    {"id": 21, "name": "Karthik", "department": "EEE", "marks": 80},
    {"id": 22, "name": "Bindu", "department": "CIVIL", "marks": 75},
    {"id": 23, "name": "Charan", "department": "ECE", "marks": 93},
    {"id": 24, "name": "Madhavi", "department": "CSE", "marks": 84},
    {"id": 25, "name": "Rakesh", "department": "MECH", "marks": 66},
    {"id": 26, "name": "Sindhu", "department": "CSE", "marks": 89},
    {"id": 27, "name": "Abhinav", "department": "EEE", "marks": 73},
    {"id": 28, "name": "Deepika", "department": "ECE", "marks": 87},
    {"id": 29, "name": "Sai", "department": "CSE", "marks": 96},
    {"id": 30, "name": "Nandini", "department": "CIVIL", "marks": 70},

    {"id": 31, "name": "Varun", "department": "CSE", "marks": 88},
    {"id": 32, "name": "Bhavana", "department": "ECE", "marks": 77},
    {"id": 33, "name": "Tarun", "department": "MECH", "marks": 82},
    {"id": 34, "name": "Ayesha", "department": "EEE", "marks": 69},
    {"id": 35, "name": "Lokesh", "department": "CIVIL", "marks": 74},
    {"id": 36, "name": "Pavani", "department": "CSE", "marks": 91},
    {"id": 37, "name": "Dheeraj", "department": "ECE", "marks": 85},
    {"id": 38, "name": "Sravani", "department": "MECH", "marks": 78},
    {"id": 39, "name": "Ajay", "department": "EEE", "marks": 81},
    {"id": 40, "name": "Mounika", "department": "CSE", "marks": 95},

    {"id": 41, "name": "Ravi", "department": "ECE", "marks": 90},
    {"id": 42, "name": "Geetha", "department": "CIVIL", "marks": 73},
    {"id": 43, "name": "Vijay", "department": "MECH", "marks": 84},
    {"id": 44, "name": "Manasa", "department": "CSE", "marks": 93},
    {"id": 45, "name": "Praneeth", "department": "EEE", "marks": 76},
    {"id": 46, "name": "Kavya", "department": "ECE", "marks": 88},
    {"id": 47, "name": "Rithvik", "department": "CSE", "marks": 97},
    {"id": 48, "name": "Sushma", "department": "CIVIL", "marks": 71},
    {"id": 49, "name": "Yash", "department": "MECH", "marks": 80},
    {"id": 50, "name": "Anjali", "department": "CSE", "marks": 94}
]


# -------------------------------------------------
# DEPARTMENT DATASET
# -------------------------------------------------

departments = [

    {"department": "CSE", "hod": "Dr. Ramesh"},
    {"department": "ECE", "hod": "Dr. Kavitha"},
    {"department": "MECH", "hod": "Dr. Prasad"},
    {"department": "EEE", "hod": "Dr. Suresh"},
    {"department": "CIVIL", "hod": "Dr. Mahesh"}
]


# -------------------------------------------------
# INSERT RECORDS WITH CONSTRAINTS
# -------------------------------------------------

print("\n================ INSERT RECORDS ================\n")

for student in students:

    primary_key_valid = constraints.check_primary_key(
        "students",
        "id",
        student["id"]
    )

    marks_valid = constraints.check_marks_domain(
        student["marks"]
    )

    if primary_key_valid and marks_valid:

        db.insert_into("students", student)


for department in departments:

    db.insert_into("departments", department)


# -------------------------------------------------
# SHOW TABLES
# -------------------------------------------------

print("\n================ SHOW TABLES ================\n")

db.show_tables()


# -------------------------------------------------
# SELECT ALL
# -------------------------------------------------

print("\n================ SELECT ALL ================\n")

db.select_all("students")


# -------------------------------------------------
# WHERE CONDITION
# -------------------------------------------------

print("\n================ WHERE CONDITION ================\n")

db.select_where(
    "students",
    "department",
    "CSE"
)


# -------------------------------------------------
# PROJECTION
# -------------------------------------------------

print("\n================ PROJECTION ================\n")

db.project_columns(
    "students",
    ["name", "marks"]
)


# -------------------------------------------------
# UPDATE RECORDS
# -------------------------------------------------

print("\n================ UPDATE OPERATION ================\n")

db.update_records(
    "students",
    "name",
    "Rajesh",
    "marks",
    99
)

db.select_where(
    "students",
    "name",
    "Rajesh"
)


# -------------------------------------------------
# DELETE RECORDS
# -------------------------------------------------

print("\n================ DELETE OPERATION ================\n")

db.delete_records(
    "students",
    "id",
    5
)

db.count_records("students")


# -------------------------------------------------
# JOIN OPERATIONS
# -------------------------------------------------

print("\n================ INNER JOIN ================\n")

joins.inner_join(
    "students",
    "departments",
    "department",
    "department"
)


# -------------------------------------------------
# AGGREGATION
# -------------------------------------------------

print("\n================ AGGREGATION ================\n")

aggregation.count("students")

aggregation.average("students", "marks")

aggregation.maximum("students", "marks")

aggregation.minimum("students", "marks")

aggregation.group_by_count(
    "students",
    "department"
)

aggregation.group_by_average(
    "students",
    "department",
    "marks"
)


# -------------------------------------------------
# INDEXING
# -------------------------------------------------

print("\n================ HASH INDEXING ================\n")

indexer.create_index(
    "students",
    "department"
)

indexer.show_index(
    "students",
    "department"
)

indexer.search_using_index(
    "students",
    "department",
    "CSE"
)


# -------------------------------------------------
# TRANSACTIONS
# -------------------------------------------------

print("\n================ TRANSACTIONS ================\n")

transaction.begin_transaction("TXN101")

transaction.commit_transaction("TXN101")

transaction.begin_transaction("TXN102")

transaction.rollback_transaction("TXN102")

transaction.show_logs()


# -------------------------------------------------
# CONCURRENCY CONTROL
# -------------------------------------------------

print("\n================ CONCURRENCY CONTROL ================\n")

concurrency.shared_lock(
    "T1",
    "Student_Record_1"
)

concurrency.exclusive_lock(
    "T2",
    "Student_Record_2"
)

concurrency.show_locks()

concurrency.release_lock(
    "T1",
    "Student_Record_1"
)

concurrency.two_phase_locking_demo()


# -------------------------------------------------
# SERIALIZABILITY
# -------------------------------------------------

print("\n================ SERIALIZABILITY ================\n")

serial_checker.sample_schedule_demo()


# -------------------------------------------------
# RECOVERY SYSTEM
# -------------------------------------------------

print("\n================ RECOVERY SYSTEM ================\n")

recovery.write_log(
    "TXN201",
    "UPDATE",
    "students",
    "marks = 89",
    "marks = 99"
)

recovery.show_logs()

recovery.undo("TXN201")

recovery.redo("TXN201")

recovery.simulate_crash()

recovery.recover_system()


# -------------------------------------------------
# NORMALIZATION
# -------------------------------------------------

print("\n================ NORMALIZATION ================\n")

normalizer.show_functional_dependencies()

normalizer.check_1nf()

normalizer.check_2nf()

normalizer.check_3nf()

normalizer.check_bcnf()

normalizer.decomposition_demo()

normalizer.lossless_join_demo()

normalizer.dependency_preservation_demo()


# -------------------------------------------------
# ER MODEL
# -------------------------------------------------

print("\n================ ER MODEL ================\n")

er.create_entity(
    "Student",
    ["StudentID", "Name", "Department"]
)

er.create_relationship(
    "Student",
    "Enrolls",
    "Course"
)

er.one_to_many(
    "Department",
    "Student"
)

er.er_to_relational_demo()

er.specialization_demo()

er.generalization_demo()


# -------------------------------------------------
# RELATIONAL ALGEBRA
# -------------------------------------------------

print("\n================ RELATIONAL ALGEBRA ================\n")

relational.selection(
    "students",
    "department",
    "ECE"
)

relational.projection(
    "students",
    ["name", "department"]
)

relational.cartesian_product(
    "students",
    "departments"
)


# -------------------------------------------------
# SQL PARSER
# -------------------------------------------------

print("\n================ SQL PARSER ================\n")

parser.parse(
    "SELECT * FROM students"
)

parser.tokenization_demo()


# -------------------------------------------------
# QUERY EXECUTOR
# -------------------------------------------------

print("\n================ QUERY EXECUTOR ================\n")

executor.execution_demo()

executor.query_plan_demo()

executor.optimization_demo()

executor.cost_estimation_demo()


# -------------------------------------------------
# STORAGE ENGINE
# -------------------------------------------------

print("\n================ STORAGE ENGINE ================\n")

storage.storage_architecture()

storage.sequential_storage("students")

storage.simulate_pages("students")

storage.heap_file_demo()

storage.hash_file_demo()

storage.indexed_file_demo()

storage.buffer_manager_demo()

storage.page_replacement_demo()

storage.disk_access_demo()


print("\n=================================================")
print("        EduDB Execution Completed")
print("=================================================\n")