from socket import socket, AF_INET, SOCK_STREAM #importing socket, IPV4 addressing with TCP connection

server_sock = socket(AF_INET, SOCK_STREAM) #create a socket object using imported socket class
server_sock.bind(('localhost', 50000)) #bind/attaching the socket object to local machine on port 50000
server_sock.listen(1) #socket is open for a single connection 

#waiting to accept client's connection 
connection = server_sock.accept() #.accept() returns the socket to communicate with client and the (IP, Port) of client
csock = connection[0] #socket to client
caddr = connection[1] #address and port of client
print("Connection successful with: ", caddr) #prints the address/port of client

#sending user's message to client 
message = input("Enter message: ") #prompts user for input
csock.send(message.encode()) #send the message via client socket in bytes via .encode()

#receiving client's message to server
resp = csock.recv(1024) #receives up to 1KB of data/message from client 
print("Client message: ", resp.decode()) #print the message after decoding the bytes 

#close the sockets 
csock.close()
server_sock.close()