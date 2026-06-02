# MiniShellX — Linux Shell Simulator

MiniShellX is a custom Linux shell built in C that demonstrates core Operating Systems concepts using Linux system calls and process management techniques.

---

## Features

- Execute Linux commands
- Command argument parsing
- Built-in commands:
  - `cd`
  - `exit`
- Background process execution using `&`
- Inter-process communication using pipes `|`
- Concurrent process handling
- UNIX process creation and execution

---

## OS Concepts Implemented

| Concept | Implementation |
|---|---|
| Process Creation | `fork()` |
| Program Execution | `execvp()` |
| Process Synchronization | `wait()` |
| Inter Process Communication | `pipe()` |
| File Descriptor Redirection | `dup2()` |
| Directory Management | `chdir()` |
| Concurrent Processes | Background jobs |
| Shell Architecture | Built-in commands |

---

## Tech Stack

- C
- Linux (WSL2 Ubuntu)
- GCC
- Makefile
- VS Code

---

## Project Structure

```bash
MiniShellX/
│
├── include/
├── screenshots/
├── src/
│   └── main.c
│
├── .gitignore
├── Makefile
└── README.md
```

---

## Build Instructions

### Compile the project

```bash
make
```

### Run the shell

```bash
make run
```

### Clean executable

```bash
make clean
```

---

## Supported Commands

### Normal Commands

```bash
ls
pwd
date
whoami
```

### Commands with Arguments

```bash
ls -l
mkdir demo
```

### Built-in Commands

```bash
cd demo
exit
```

### Background Processes

```bash
sleep 10 &
```

### Pipes

```bash
ls | grep src
```

---

## Sample Output

```bash
myshell> ls -l
myshell> pwd
myshell> sleep 10 &
myshell> ls | grep src
myshell> exit
```

---

## Learning Outcomes

This project helped strengthen practical understanding of:

- Operating Systems
- Linux internals
- Process management
- Process synchronization
- Inter-process communication
- UNIX system calls
- Shell architecture
- Concurrent execution

---

## Author

Sameer Shaik

---
