import socket 
import select
import sys

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print("USAGE: python chat_client.py IP port number")
    exit()

IP = str(sys.argv[1])

Port = int(sys.argv[2])

server.connect((IP,Port))

while 1: 
    socket_list = [sys.stdin, server]

    read_sockets,write_socket,error_socket = select.select(socket_list,[],[])

    for s in read_sockets:
        if s == server:
            msg = s.recv(2048)
            print msg
        else: 
            msg = sys.stdin.readline()
            server.send(msg)
            sys.stdout.write("<YOU>")
            sys.stdout.write(msg)
            sys.stdout.flush()

server.close()
