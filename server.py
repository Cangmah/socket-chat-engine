from socket import socket, AF_INET, SOCK_STREAM #importing socket, IPV4 addressing with TCP connection
import threading #thread library to run send() and receive() simultaneously 

#sending user's message to client 
#send function to call via threading on client socket
def send(csock):
    while (True): #continuously sends user's input to client until user 'quit' the connection
        message = input("Enter message: ") #prompts user for input
        if (message == "quit"):
            break
        csock.send(message.encode()) #send the message via client socket in bytes via .encode()

#receiving client's message to server on client socket
def receive(csock):
    while(True):
        resp = csock.recv(1024) #receives up to 1KB of data/message from client
        if (resp == b"quit" or resp == b''): #if user input is quit or empty, end 
            break 
        print("Client message: ", resp.decode()) #print the message after decoding the bytes 

server_sock = socket(AF_INET, SOCK_STREAM) #create a socket object using imported socket class
server_sock.bind(('localhost', 50000)) #bind/attaching the socket object to local machine on port 50000
server_sock.listen(1) #socket is open for a single connection 

#waiting to accept client's connection 
connection = server_sock.accept() #.accept() returns the socket to communicate with client and the (IP, Port) of client
csock = connection[0] #socket to client
caddr = connection[1] #address and port of client
print("Connection successful with: ", caddr) #prints the address/port of client

#creating two threads for sending and receiving messages to client 
#target is the function name and args is the function argument as tuple
t1 = threading.Thread(target=send, args=(csock,)) 
t2 = threading.Thread(target=receive, args=(csock,))
#start threads 
t1.start()
t2.start()
#main waits for threads to exit before closing sockets 
t1.join()
t2.join()
#close the sockets 
csock.close()
server_sock.close()