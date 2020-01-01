import socket
import select
import sys 
from thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

if len(sys.argv) != 3: 
    print("Usage: python chat_server.py IP port number")
    exit()

IP = str(sys.argv[1])

Port = int(sys.argv[2])

server.bind((IP,Port))

server.listen(100)

client_list = []

def clientthread(conn, addr):
    conn.send("Welcome to this chatroom!")
    
    while 1==1:
        try:
            msg = conn.recv(2048)
            if msg: 
                print("<" + addr[0] + ">" + msg)
                outgoingMsg = "<" + addr[0] + "> " + msg
                broadcast(outgoingMsg,conn)
            else:
                remove(conn)
        except:
            continue

def broadcast(msg, conn):
    for client in client_list:
        if client != conn:
            try:
                client.send(msg)
            except: 
                client.close()
                remove(clients)

def remove(conn):
    if conn in client_list:
        client_list.remove(conn)

while 1==1:
    conn, addr = server.accept()

    client_list.append(conn)

    print addr[0] + " connected"

    start_new_thread(clientthread,(conn,addr))

conn.close()
server.close()
