import socket, Queue, signal
import sys
from thread import *
global ALIVE
ALIVE = True

#Function for handling connections. This will be used to create threads
def clientthread(quu,):
	global ALIVE
	while ALIVE:
		blocked = True
		while blocked:
			blocked = False
			try: 
				connectionTuple = quu.get()
			except Queue.Empty as emp:		
				blocked = True

		conn = connectionTuple[0]
		addr = connectionTuple[1]
		print 'Connected with ' + addr[0] + ':' + str(addr[1])

		while True:
			data = conn.recv(1024)		
			if data=="HELO text\n":
				reply = "HELO text\nIP:"+str(addr[0])+"\nPort:"+str(PORT)+"\nStudentID:11816252"			
			elif data=="KILL_THREAD\n":
				break
			elif data=="KILL_SERVICE\n":
				reply = "panic"
				ALIVE = False
				break
			elif data is None:
				break
			else:
				reply = data.upper()			
			conn.send(reply)
		conn.close()

#MAIN

HOST = ''
PORT = int(sys.argv[1]) #paramterised port number
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
quu = Queue.Queue()

try:
	s.bind((HOST, PORT))
except socket.error as msg:
	print 'Bind failed'
	sys.exit()

s.listen(5)
print 'Socket now listening'

for x in range(0, 10):
	start_new_thread(clientthread, (quu,))
while ALIVE:
	print str(ALIVE)	
	conn, addr = s.accept()
	quu.put((conn,addr))
s.close()
