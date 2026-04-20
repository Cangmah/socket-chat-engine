# socket-chat-engine

A chat application built with TCP sockets in Python, developed for CIS 457 – Data Communications at Grand Valley State University (Winter 2026).

## Overview

This project demonstrates the fundamentals of socket programming by implementing a client-server chat system. Communication between the client and server is established over TCP sockets using Python's built-in `socket` library.

## Part 1 – Basic Client-Server Message Exchange

The first component of this project establishes a simple one-round communication between a client and a server:

- The **server** starts and listens for an incoming connection on a specified port.
- The **client** connects to the server using its IP address and port.
- The **server** prompts the user to type a message, which is sent to the client.
- The **client** receives the message, displays it, then prompts the user to type a reply, which is sent back to the server.
- Both programs terminate after the exchange is complete.

No threading or external libraries are required — only Python's standard `socket` module.

## Part 2 – Continuous Chat with Multithreading

The second component expands on Part 1 by keeping both the client and server online after each message, allowing them to chat indefinitely:

- Both the **client** and **server** remain connected after each message is sent.
- Either side can send **multiple messages in a row** without waiting for a reply.
- **Multithreading** is used to handle sending and receiving simultaneously — one thread listens for incoming messages while the other waits for user input.
- The chat continues until the connection is manually terminated.

Uses Python's standard `socket` and `threading` modules.

## Part 3 – Group Chat with Multiple Clients

The third component redesigns the server into a pure message relay — the server no longer participates in the chat, it only routes messages between connected clients:

- The **server** accepts multiple clients simultaneously and relays every message to all connected clients.
- The **server** has no user input — it only listens and broadcasts.
- The **client** program is the same for all users — simply run the same `client.py` multiple times to simulate multiple users.
- Every message sent by one client is shown to **all connected clients** (group chat).

Uses Python's standard `socket` and `threading` modules.

## Requirements

- Python 3.x
- No external dependencies (uses Python standard library only)

## Usage

### Start the server

```bash
python3 server.py
```

The server will start listening for incoming client connections on port `50000`. It does not send messages — it only relays messages between connected clients.

### Start the clients

Open a **separate terminal for each client** and run the same `client.py` file in each:

```bash
python3 client.py
```

To simulate a group chat on the same machine, open multiple terminals and run `client.py` in each one. Messages sent from one client will be broadcast to all other connected clients.

### Running on two different machines

To connect clients from a different machine, both machines must be on the **same network**.

1. Find the server machine's local IP address:
```bash
networksetup -getinfo Wi-Fi
```

2. On the client machine, open `client.py` and update the `connect()` line with the server's IP address:
```python
client_sock.connect(('192.168.x.x', 50000))  # replace with server machine's IP
```

3. Run `server.py` on the server machine and `client.py` on the client machine — they will communicate over the local network.

## Project Structure

```
socket-chat-engine/
├── server.py   # Server-side socket program
├── client.py   # Client-side socket program
└── README.md
```
