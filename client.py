import socket, sys
import time
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = int(sys.argv[1]) # Arbitrary non-privileged port
clientsocket.connect(('localhost', PORT))
while True:
	message = raw_input("What Message Are You Sending\n")
	message += '\n'
	if message is None:
		break
	clientsocket.send(message)
	reply = clientsocket.recv(1024)
	print reply

clientsocket.close()
