#!/usr/bin/python

import socket
import sys
import argparse
import os
import time
import threading

host_name = socket.gethostname()
ip_addr = socket.gethostbyname(host_name)
host = ip_addr
data_payload = 2048
backlog = 5

def echo_server(port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_address = (host,port)
	print "Starting up echo server on %s port %s" % server_address
	sock.bind(server_address)
	sock.listen(backlog)
	while True:
		print "Wating to receive message from client"
		client, address = sock.accept()
		t = threading.Thread(target=tcplink,args=(client,address))
		t.start()
		t.join()
		
def tcplink(client,addr):
	print "Accept new conn from %s:%s..." %addr
	while True:
		data = client.recv(data_payload)
		time.sleep(1)
		print "recv data: %s" %data
#		if data == 'exit':
#			print "will stop"
#			break
	print "will close"
	client.close()
	print 'Connection from %s:%s closed.' %addr

parser = argparse.ArgumentParser(description='Socket Server Example')
parser.add_argument('--port', action="store", dest='port', type=int, required=True)
given_args = parser.parse_args()
port = given_args.port
echo_server(port)

