import socket
import sys

#create a connection to the server app
tcp_socket = socket.create_connection(("localhost", 9000))

try:
    print("tcp_socket: ", tcp_socket)
    data = tcp_socket.recv(1024)
    print(f"Recieved: {data}")

finally:
    print("Closing socket")
    tcp_socket.close()
