#tcp client

import socket
socket1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('localhost',12345)
socket1.connect(server_address)

message=eval(input("Enter message:"))
	
 
socket1.sendall(message.encode())

data,adress =socket1.recvfrom(1024)
print(f'Recieved data:{data.decode()}')


 

# socket1.close()
