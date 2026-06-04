# EduDB — Educational Relational DBMS Engine

EduDB is a Python-based Educational Database Management System developed to practically demonstrate major GATE DBMS concepts through modular implementations.

This project focuses on understanding how relational databases work internally by implementing concepts such as relational algebra, transactions, concurrency control, indexing, normalization, query processing, recovery systems, ER modeling, and storage architecture.

---

# Features

## Core Database Operations
- CREATE TABLE
- INSERT INTO
- SELECT *
- WHERE filtering
- UPDATE records
- DELETE records
- Projection operation
- Table listing
- Record counting

---

## SQL & Query Processing
- SQL Query Parsing
- Query Tokenization
- Query Validation
- Query Execution Engine
- Query Plan Simulation
- Query Optimization Concepts
- Cost Estimation Demo

---

## Relational Algebra Operations
- Selection
- Projection
- Union
- Intersection
- Difference
- Cartesian Product
- Rename Operation
- Division Operation Concept

---

## Constraint Management
- Primary Key Constraints
- Foreign Key Constraints
- Unique Constraints
- NOT NULL Constraints
- Domain Constraints

---

## Join Operations
- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- Nested Loop Join

---

## Aggregation Operations
- COUNT
- SUM
- AVG
- MIN
- MAX
- GROUP BY COUNT
- GROUP BY AVG

---

## Indexing
- Hash Indexing
- Indexed Search
- Index Creation
- Index Deletion

---

## Transaction Management
- BEGIN TRANSACTION
- COMMIT
- ROLLBACK
- Transaction Logging

---

## Concurrency Control
- Shared Locks
- Exclusive Locks
- Lock Table
- Two Phase Locking (2PL)

---

## Serializability
- Conflict Serializability
- Precedence Graph
- Cycle Detection
- Schedule Analysis

---

## Recovery System
- Write Ahead Logging (WAL)
- Recovery Logs
- UNDO Operations
- REDO Operations
- Crash Recovery Simulation

---

## Normalization
- Functional Dependencies
- 1NF
- 2NF
- 3NF
- BCNF
- Lossless Join
- Dependency Preservation

---

## ER Modeling
- Entities
- Attributes
- Relationships
- One-to-One Relationships
- One-to-Many Relationships
- Many-to-Many Relationships
- Weak Entities
- ER-to-Relational Mapping
- Specialization & Generalization

---

## Storage Engine Concepts
- Sequential File Organization
- Heap File Organization
- Hash File Organization
- Indexed File Organization
- Page / Block Simulation
- Buffer Manager Concepts
- Page Replacement Concepts

---

# GATE DBMS Concepts Covered

| Topic | Implemented |
|---|---|
| Relational Model | ✅ |
| Relational Algebra | ✅ |
| SQL Operations | ✅ |
| CRUD Operations | ✅ |
| Query Processing | ✅ |
| Query Optimization | ✅ |
| Constraints | ✅ |
| Primary Keys | ✅ |
| Foreign Keys | ✅ |
| Functional Dependencies | ✅ |
| Normalization | ✅ |
| Transactions | ✅ |
| Concurrency Control | ✅ |
| Serializability | ✅ |
| Recovery System | ✅ |
| Indexing | ✅ |
| Storage Architecture | ✅ |
| ER Modeling | ✅ |
| File Organization | ✅ |

---

# Project Structure

```text
EduDB/
│
├── data/
├── docs/
├── schemas/
├── screenshots/
│
├── engine/
│   ├── database.py
│   ├── parser.py
│   ├── executor.py
│   ├── storage.py
│   ├── indexer.py
│   ├── joins.py
│   ├── aggregation.py
│   ├── normalizer.py
│   ├── constraints.py
│   ├── concurrency.py
│   ├── serializability.py
│   ├── recovery.py
│   ├── transaction.py
│   ├── er_model.py
│   └── relational_algebra.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Tech Stack

- Python
- JSON Storage
- VS Code

---

# Requirements

EduDB uses only Python standard libraries.

No external packages are required.

Example `requirements.txt`:

```text
# No external dependencies required
# Built using Python standard libraries only
```

---

# How to Run

## 1. Clone Repository

```bash
git clone <repository-link>
```

---

## 2. Navigate to Project

```bash
cd EduDB
```

---

## 3. (Optional) Delete Old Generated Data Files

If old execution files already exist inside the `data/` folder, remove them before running again.

### Windows PowerShell

```powershell
Remove-Item data\*.json
```

### Linux / Ubuntu / Mac

```bash
rm data/*.json
```

---

## 4. Run Project

### Windows

```bash
python main.py
```

### Linux / Ubuntu / Mac

```bash
python3 main.py
```

---

# Sample Modules Demonstrated

- Relational Algebra Operations
- Join Processing
- Query Execution
- Aggregation Functions
- Indexing
- Transactions
- Concurrency Control
- Serializability Checking
- Recovery Mechanisms
- Normalization Analysis
- ER Modeling
- Storage Architecture

---

# Learning Outcomes

This project helped in understanding:

- Internal architecture of DBMS systems
- Query processing workflow
- Relational algebra implementation
- Transaction handling
- Concurrency management
- Recovery mechanisms
- Indexing concepts
- Storage organization
- Schema normalization
- ER-to-Relational conversion

---

# Future Improvements

- B+ Tree Indexing
- Query Optimizer
- SQL CLI Interface
- Buffer Pool Manager
- Query Cost Optimizer
- Advanced Parsing
- Deadlock Detection
- Multi-user Transaction Simulation

---

# Author

Sameer Shaik
