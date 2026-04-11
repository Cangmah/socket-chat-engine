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

## Requirements

- Python 3.x
- No external dependencies (uses Python standard library only)

## Usage

### Start the server

```bash
python server.py
```

The server will begin listening for a connection. Once connected, you will be prompted to type a message.

### Start the client

```bash
python client.py
```

The client will connect to the server. After receiving the server's message, you will be prompted to type a reply.

> Both programs can be run on the same machine using `localhost` as the server address.

## Project Structure

```
socket-chat-engine/
├── server.py   # Server-side socket program
├── client.py   # Client-side socket program
└── README.md
```
