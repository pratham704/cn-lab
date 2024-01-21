
import socket

def start_udp_client():
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	server_port = ('localhost', 12345)

	while True:
		# Get user input for the message
		message = input("Enter message to send: ")
		# Send the message to the server
		client_socket.sendto(message.encode(), server_port)
  
		recieved_from_server , address = client_socket.recvfrom(1024)
		print(f"Received message from {address}: {recieved_from_server.decode()}")

if __name__ == "__main__":
	start_udp_client()
