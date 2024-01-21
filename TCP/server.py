import socket

socket1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_port=('localhost',12345)
socket1.bind(server_port)

socket1.listen(5)


print("TCP server is waiting for connections....")

while True:
	client_socket,client_address=socket1.accept()
	print(f'connected to{client_address}')

	data=client_socket.recv(1024)
	if data:
			print(f'Recieved data:{data.decode()}')
			client_socket.sendall(data)
	
