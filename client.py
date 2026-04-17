from socket import socket, AF_INET, SOCK_STREAM #import socket class and constants 
import threading #use thread to send/receive messages to server simultaneously

#client receiving message, continuously prints it unless quit 
#use try/except to ensure smooth quit without receiver throwing error once socket closes
def receive(client_sock):
    while(True):
        try: 
            resp = client_sock.recv(1024) #receives 1KB of data from server
            if (resp == b''): #exit if no connection
                client_sock.close()
                break #if quit, stop receiving exit loop
            print( resp.decode()) #print decoded message
        except:
            break
#client sends message to server continuously
def send(client_sock):
    while(True):
        message = input()
        if(message == 'quit'):
            client_sock.close()
            break #exit loop if quit 
        try: #avoid error if socket has closed from server side using try/except, instead break cleanly
            client_sock.send(message.encode()) #send encoded message to server
        except:
            break

#creating client socket and connect to server
client_sock = socket(AF_INET, SOCK_STREAM) #create client's socket object 
client_sock.connect(('localhost', 50000)) #establish a connection to server socket 

#create threads and start for both functions
t1 = threading.Thread(target=receive, args=(client_sock,))
t2 = threading.Thread(target=send, args=(client_sock,))

#start threads
t1.start()
t2.start()
#end main after threads ends
t1.join()
t2.join()
