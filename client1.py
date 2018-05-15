import socket
import sys
import time

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = input("enter the host to connect!!!!!!!")
port = int(input("enter the port!!!!!"))

try:
	sock.connect((host,port))
	print("client connected at the time",time.ctime())
except Exception as e:
	print(str(e))

ack = 1
def send_data(sock,ack):
	while True:
		try:
			data = sock.recv(1024).decode('utf-8')
			if not data:
				break
			print(data)
			send_datas = "ACK"+':'+str(ack)
			sock.send(send_datas.encode('utf-8'))
			ack+=1
			time.sleep(0.5)
		except Exception as e:
			print(str(e))
			sock.close()
			sys.exit(0)
		except KeyboardInterrupt as e:
			print("connection closed")
			sock.close()
			sys.exit(0)

send_data(sock,ack)