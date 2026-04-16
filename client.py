from socket import socket, AF_INET, SOCK_STREAM #import socket class and constants 

client_sock = socket(AF_INET, SOCK_STREAM) #create client's socket object 
client_sock.connect(('localhost', 50000)) #establish a connection to server socket 
resp = client_sock.recv(1024) #receives message from server 
print("Server says: ", resp.decode()) #print server's message decoding the byte to string

#sending a response message to server
message = input("Input message: ") #get input from user
client_sock.send(message.encode()) #send the input as encoded string to byte 

#close the socket
client_sock.close()
