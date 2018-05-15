import socket
import time
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
host = socket.gethostbyname(host)

port = int(input("enter the port"))
sock.bind((host,port))

sock.listen(5)

print("Server start listening at ip",host,"port"+str(port))

try:
	client_sock,addr = sock.accept()
	print("client conneted at ip",addr[0]+"port"+str(addr[1]))
except Exception as e:
	print(str(e))
	sock.close()
	sys.exit(0)

pack = 1 

def send_data(client_sock,pack):
	while True:
		try:
			send_datas = "packet"+' '+str(pack)
			client_sock.send(send_datas.encode('utf-8'))
			pack+=1
			data = client_sock.recv(1024).decode('utf-8')
			if not data:
				break
			print(str(data))
		except Exception as e:
			print(str(e))
			sock.close()
			sys.exit(0)
		except KeyboardInterrupt as e:
			print("closing server!!!!")
			sys.exit(0)
		except ConnectionResetError as e:
			print("Connection closed by the server!!!!")
			sock.close()
			sys.exit(0)

send_data(client_sock,pack)

