import socket
import sys

#create a connection to the server app
tcp_socket = socket.create_connection(("localhost", 9000))

try:
    print("tcp_socket: ", tcp_socket)
    navy = "Navy"
    data = navy.encode()
    tcp_socket.sendall(data)
    answer = tcp_socket.recv(1024)
    print(f"Recieved: {answer}")

finally:
    print("Closing socket")
    tcp_socket.close()
