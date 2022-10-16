"""Example CTF Client"""
import socket


class CTFException(Exception):
    """Custom class for our own Exceptions."""

    def __init__(self, msg: str):
        super().__init__(msg)
        self.msg = msg


class CTFClient:
    """Simple CTF client for reading and solving TCP server-type challenges."""

    def __init__(self, targ_ip: str, targ_port: int, buf_size: int = 1024):
        """Create the client by initializing the connection.

        :param targ_ip: Target IP address
        :param targ_port: Target port number
        :param buf_size: Size of buffer to read per recv call
        :raises CTFException: if the connection failed
        """
        self.targ_ip = targ_ip
        self.targ_port = targ_port
        self.buf_size = buf_size
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Try connecting to the server
        try:
            self.sock.connect((targ_ip, targ_port))
        except ConnectionRefusedError as error:
            raise CTFException(
                "Connection refused! Please double-check the IP and port values "
                "and make sure the server is running!"
            ) from error

    def __del__(self):
        """Clean up any leftover sockets."""
        if self.sock:
            self.sock.close()

    def send_data(self, data: str):
        """Converts and sends the given data to the server through
        the connected socket.

        :param data: Data to send to the server
        :raises CTFException: if the socket failed to send (maybe closed!)
        """
        self.sock.sendall(data.encode())

    def get_data(self) -> str:
        """Receives and returns any buffered data from the connected
        socket; there may be more data than returned here, so consider
        calling this method repeatedly if you know the server has sent
        more information.

        :returns: Data from the server
        :raises CTFException: if the socket failed to receive (maybe closed!)
        """
        return self.sock.recv(self.buf_size).decode()
