# NetStreamX — Computer Networks Laboratory

NetStreamX is a Python-based Computer Networks project developed to practically implement and demonstrate core GATE Computer Networks concepts through hands-on simulations and network programming.

The project focuses on understanding networking fundamentals by building real implementations of TCP communication, UDP communication, HTTP servers, DNS resolution, routing mechanisms, and packet transmission.

---

# Features

## TCP Communication
- TCP Client-Server Architecture
- Reliable Message Exchange
- Socket Programming
- Port-Based Communication

---

## Multi-Client Chat Server
- Concurrent Client Connections
- Message Broadcasting
- Thread-Based Client Handling
- TCP-Based Communication

---

## UDP Communication
- Connectionless Communication
- Datagram Transmission
- UDP Client-Server Model

---

## HTTP Server
- Basic HTTP Server
- GET Request Handling
- HTML Response Generation
- Browser-Server Communication

---

## DNS Lookup
- Domain Name Resolution
- Hostname to IP Conversion
- DNS Concepts Demonstration

---

## Routing Simulation
- Routing Tables
- Next-Hop Selection
- Packet Forwarding Logic
- Network Layer Concepts

---

## Packet Simulation
- Source Address
- Destination Address
- Protocol Field
- Payload Handling

---

# Computer Networks Concepts Covered

| Topic | Implemented |
|---------|---------|
| TCP | ✅ |
| UDP | ✅ |
| Socket Programming | ✅ |
| Client-Server Architecture | ✅ |
| Multi-Client Communication | ✅ |
| HTTP Protocol | ✅ |
| DNS | ✅ |
| Routing | ✅ |
| Packet Simulation | ✅ |
| OSI Model | ✅ |
| TCP/IP Model | ✅ |
| IP Addressing | ✅ |
| Ports | ✅ |

---

# Project Structure

```text
NetStreamX/
│
├── client/
│   ├── __init__.py
│   ├── tcp_client.py
│   └── udp_client.py
│
├── server/
│   ├── __init__.py
│   ├── tcp_server.py
│   ├── udp_server.py
│   └── http_server.py
│
├── protocols/
│   ├── __init__.py
│   ├── packet.py
│   ├── dns_lookup.py
│   └── routing.py
│
├── docs/
│   ├── tcp_notes.md
│   ├── udp_notes.md
│   ├── http_notes.md
│   ├── dns_notes.md
│   ├── routing_notes.md
│   ├── socket_programming_notes.md
│   ├── tcp_vs_udp.md
│   ├── osi_tcpip_notes.md
│   ├── dns_practical_notes.md
│   ├── routing_practical_notes.md
│   └── packet_notes.md
│
├── screenshots/
│
├── tests/
│   ├── __init__.py
│   ├── test_dns.py
│   ├── test_packet.py
│   └── test_routing.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Requirements

No external dependencies are required.

The project is built entirely using Python Standard Libraries.

Example:

```bash
Python 3.10+
```

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate into the project:

```bash
cd NetStreamX
```

---

# Running the Project

## Project Overview

```bash
python main.py
```

---

## TCP Server

```bash
python server/tcp_server.py
```

---

## TCP Client

```bash
python client/tcp_client.py
```

---

## UDP Server

```bash
python server/udp_server.py
```

---

## UDP Client

```bash
python client/udp_client.py
```

---

## HTTP Server

```bash
python server/http_server.py
```

Open:

```text
http://127.0.0.1:8080
```

---

## DNS Lookup

```bash
python protocols/dns_lookup.py
```

---

## Routing Simulation

```bash
python protocols/routing.py
```

---

## Packet Simulation

```bash
python protocols/packet.py
```

---

# Running Tests

```bash
python tests/test_dns.py
python tests/test_packet.py
python tests/test_routing.py
```

---

# Learning Outcomes

This project helped strengthen practical understanding of:

- Computer Networks
- TCP/IP Communication
- Socket Programming
- Client-Server Architecture
- HTTP Protocol
- DNS Resolution
- Routing Mechanisms
- Packet Transmission
- Network Programming in Python

---

# GATE CS Practical Implementations

NetStreamX is part of the larger **GATE-CS-Practical-Implementations** repository, where core Computer Science subjects are implemented through practical projects.

Completed Subjects:

- Operating Systems → MiniShellX
- Database Management Systems → MiniDB-EduDB
- Computer Networks → NetStreamX

---

# Author

Sameer Shaik

Computer Networks Laboratory Project for GATE CS & Core Computer Science Learning.