
import socket


def start_udp_server():
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	server_port = ('localhost', 12345)
	server_socket.bind(server_port)
	

	while True:
		print("Waiting for a message from the client...")
		data, client_address = server_socket.recvfrom(1024)
		print(f"Received message from {client_address}: {data.decode()}")
  
		server_socket.sendto(data, client_address)
  
		

if __name__ == "__main__":
	start_udp_server()
