#!/usr/bin/env python

from pyfiglet import Figlet
f = Figlet(font='slant')
print f.renderText('tcps3rv')

print '##### TCP Server #####'
print '##### By c4b3rw0lf #####'

import socket
import threading 

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print "[*] tcps3rv is now listening on %s:%d" % (bind_ip,bind_port)

# This is our client-handling tread
def handle_client(client_socket):

    # print out what the client sends
    request = client_socket.recv(1024)
    print "[*] Received: %s" % request
    
    # send back a packet
    client_socket.send("ACK!")
    client_socket.close()

while True:
     client,addr = server.accept()
     print "[*] Connection accepted from: %s:%d" % (addr[0],addr[1])

     # let the client thread handle incoming data
     client_handler = threading.Thread(target=handle_client,args=(client,))
     client_handler.start()
