import unittest
from unittest.mock import patch

import mysql.connector
import io

from SERVER.PuTTY_server.server import handle_client

class TestStartDB(unittest.TestCase):

    def test_start_DB(self):
        host = "localhost"
        user = "omega_admin"
        password = "123"

        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )

        self.assertIsNotNone(connection)
        self.assertTrue(connection.is_connected())

class TestServer(unittest.TestCase):

    def test_handle_client(self):
        connection = "test_connection"
        expected_output = "Test message.\n"

        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            conn = io.StringIO("Test message.\n")
            handle_client(conn, "test_addr", connection)

        self.assertEqual(fake_stdout.getvalue(), expected_output)
