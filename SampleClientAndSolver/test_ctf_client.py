"""CTF Client Tests"""

import socket

import pytest

import ctf_client


class TestCTFClient:
    """Group of tests for simple CTF client"""

    # pylint: disable=attribute-defined-outside-init
    def setup(self):
        """Spin up a test server."""
        self.port = 7777
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("localhost", self.port))
        self.server.listen(0)

    def teardown(self):
        """Shutdown our test server."""
        self.server.close()

    def test_connect_good(self):
        """Successful TCP connection"""
        _ = ctf_client.CTFClient("localhost", self.port)

    def test_connect_bad(self):
        """Failed TCP connection"""
        with pytest.raises(ctf_client.CTFException):
            _ = ctf_client.CTFClient("localhost", self.port + 1)

    def test_get(self):
        """Receive some TCP data"""
        client = ctf_client.CTFClient("localhost", self.port)
        conn, _ = self.server.accept()
        conn.sendall("blah".encode())
        assert client.get_data() == "blah"
        conn.sendall("another blah".encode())
        assert client.get_data() == "another blah"

    def test_send(self):
        """Send some TCP data"""
        client = ctf_client.CTFClient("localhost", self.port)
        client.send_data("yadda")
        conn, _ = self.server.accept()
        assert conn.recv(1024) == b"yadda"
        client.send_data("yadda yadda")
        assert conn.recv(1024) == b"yadda yadda"
