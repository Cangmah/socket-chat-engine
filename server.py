from socket import socket, AF_INET, SOCK_STREAM #importing socket, IPV4 addressing with TCP connection
import threading #thread library to run send() and receive() simultaneously 

#empty list of clients storing their IP and Port
client_list = []

#function for accepting clients to server socket
def clients(server_sock):
    while (True): #continuously accept clients and add to the list of clients
        client = server_sock.accept()
        client_list.append(client) #add client both socket and address/port as tuple to the list
        print("Client connected", client[1]) #print client's address/port
        #create a thread for client to listen and broadcast message
        threading.Thread(target=client_control, args=(client,)).start()

#used by thread, controls the listening and broadcasting by a client from the client list

def client_control(client):
    while (True):
        try: #try/except to ensure client is online, else remove from list and break
            resp = client[0].recv(1024) #listens to the client using its socket from tuple[0]  list
            if (resp == b''): client_list.remove(client);break #if client disconnects, remove from list and break
            #Go through each client in the list, and send message to everyone but current client
            for c in client_list:
                if(c[1] != client[1]): #ensure message is sent to everyone in the list but current client itself
                    c[0].send(f"{client[1]}: ".encode() + resp) #attach sender's address/port to the message(resp)

        except: #if client disconnects or offline, remove from list of clients and break
            client_list.remove(client)
            break

#create a socket object using imported socket class
server_sock = socket(AF_INET, SOCK_STREAM) 
server_sock.bind(('localhost', 50000)) #bind/attaching the socket object to local machine on port 50000
server_sock.listen(10) #socket is open for up to 10 connections

#create thread for client
#use try/except to account for shutting down server (ctrl+C)
try:
    clients(server_sock)
except KeyboardInterrupt:
    print("Server shutting down...goodbye")
    server_sock.close()
