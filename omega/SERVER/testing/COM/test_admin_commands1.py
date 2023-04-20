import io
import sqlite3
import unittest
from io import StringI, StringIO
from unittest.mock import MagicMock, patch, call

from SERVER.DB_client.CRUD import admin_CRUD, autor_CRUD
from SERVER.PuTTY_server import send_read_PuTTY
from SERVER.admin.admin_commands1 import C_admin, R_admin, D_admin, C_autor


class TestC_admin(unittest.TestCase):

    def setUp(self):
        self.connection = MagicMock()
        self.conn = MagicMock()
        self.addr = MagicMock()

    def test_C_admin(self):
        input_values = ['Karel\n', 'Novak\n', 'karel123\n', 'heslo123\n']
        output = StringIO()
        send_mock = MagicMock(side_effect=lambda msg, conn, addr: output.write(msg))
        read_mock = MagicMock(side_effect=input_values)
        C_admin.send_read_PuTTY.send = send_mock
        C_admin.send_read_PuTTY.read = read_mock

        C_admin.C_admin(self.connection, self.conn, self.addr)

        expected_output = "Napište křestní jméno admina: Napište příjmení admina: Napište přihlašovací jméno admina: Napište heslo admina: Admin vytvořenDone"
        self.assertEqual(output.getvalue(), expected_output)

    def test_C_admin_exception(self):
        input_values = ['Karel\n', 'Novak\n', 'karel123\n', 'heslo123\n']
        output = StringIO()
        send_mock = MagicMock(side_effect=lambda msg, conn, addr: output.write(msg))
        read_mock = MagicMock(side_effect=input_values)
        create_mock = MagicMock(side_effect=Exception("Test exception"))
        C_admin.send_read_PuTTY.send = send_mock
        C_admin.send_read_PuTTY.read = read_mock
        C_admin.admin_CRUD.create = create_mock

        C_admin.C_admin(self.connection, self.conn, self.addr)

        self.assertEqual(output.getvalue(),
                         "Napište křestní jméno admina: Napište příjmení admina: Napište přihlašovací jméno admina: Napište heslo admina: Error: AC002")


class TestR_admin(unittest.TestCase):
    def setUp(self):
        self.connection = MagicMock()
        self.conn = MagicMock()
        self.addr = MagicMock()
        self.expected_output = "[(1, 'John', 'Doe', 'johndoe', 'password')]\n"

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout):
        R_admin(self.connection, self.conn, self.addr)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_R_admin_successful(self):
        admin_CRUD.read = MagicMock(return_value=[(1, 'John', 'Doe', 'johndoe', 'password')])
        self.assert_stdout(self.expected_output)

    def test_R_admin_unsuccessful(self):
        admin_CRUD.read = MagicMock(side_effect=Exception('Database error'))
        expected_output = "Error: AR001\n"
        self.assert_stdout(expected_output)


class TestUAdmin(unittest.TestCase):

    def setUp(self):
        # Set up a mock connection object
        self.connection = MagicMock()

        # Set up a mock socket object
        self.socket = MagicMock()
        self.address = ('127.0.0.1', 12345)

        # Set up mock inputs for the send_read_PuTTY function
        self.inputs = ['sloupec', '1', 'new_value']

    @patch('module_with_functions.send_read_PuTTY.read')
    @patch('module_with_functions.send_read_PuTTY.send')
    def test_update_admin_successful(self, mock_send, mock_read, module_with_functions=None):
        # Set up the mock inputs for the read function
        mock_read.side_effect = self.inputs

        # Call the function being tested
        module_with_functions.U_admin(self.connection, self.socket, self.address)

        # Check that the send function was called with the expected messages
        expected_messages = ['Napište sloupec: ', 'Napište id: ', 'Napište novou proměnnou: ', 'Done']
        for call_args in mock_send.call_args_list:
            message = call_args[0][0]
            self.assertIn(message, expected_messages)
            expected_messages.remove(message)

        # Check that the update function was called with the expected arguments
        self.connection.cursor.assert_called_once()
        self.connection.cursor().execute.assert_called_once_with("UPDATE admin SET sloupec = 'new_value' WHERE id = 1;")
        self.connection.commit.assert_called_once()

    @patch('module_with_functions.send_read_PuTTY.read')
    @patch('module_with_functions.send_read_PuTTY.send')
    def test_update_admin_error(self, mock_send, mock_read, module_with_functions=None):
        # Set up the mock inputs for the read function
        mock_read.side_effect = self.inputs

        # Set up the mock objects to simulate an error when updating the admin
        self.connection.cursor().execute.side_effect = Exception()

        # Call the function being tested
        module_with_functions.U_admin(self.connection, self.socket, self.address)

        # Check that the send function was called with the expected error message
        mock_send.assert_called_once_with("Error: AU001", self.socket, self.address)

        # Check that the update function was called with the expected arguments
        self.connection.cursor.assert_called_once()
        self.connection.cursor().execute.assert_called_once_with("UPDATE admin SET sloupec = 'new_value' WHERE id = 1;")
        self.connection.commit.assert_not_called()


class TestDAdmin(unittest.TestCase):

    @patch("send_read_PuTTY.send")
    @patch("send_read_PuTTY.read")
    def test_D_admin_success(self, mock_read, mock_send):
        mock_conn = MagicMock()
        mock_addr = MagicMock()
        mock_read.side_effect = ["1", ""]

        mock_cursor = MagicMock()
        mock_cursor.execute.return_value = None
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor

        D_admin(mock_connection, mock_conn, mock_addr)

        mock_cursor.execute.assert_called_once_with("DELETE FROM admin WHERE id_admin = %s", (1,))
        mock_connection.commit.assert_called_once()
        mock_send.assert_called_once_with("Done", mock_conn, mock_addr)

    @patch("send_read_PuTTY.send")
    @patch("send_read_PuTTY.read")
    def test_D_admin_error(self, mock_read, mock_send):
        mock_conn = MagicMock()
        mock_addr = MagicMock()
        mock_read.side_effect = ["1", ""]

        mock_cursor = MagicMock()
        mock_cursor.execute.side_effect = Exception("Test exception")
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor

        D_admin(mock_connection, mock_conn, mock_addr)

        mock_cursor.execute.assert_called_once_with("DELETE FROM admin WHERE id_admin = %s", (1,))
        mock_connection.rollback.assert_called_once()
        mock_send.assert_called_once_with("Error AD001", mock_conn, mock_addr)


class TestCAutor(unittest.TestCase):

    def test_create_autor_successful(self):
        connection_mock = MagicMock()
        connection_mock.cursor().rowcount = 1
        conn_mock = MagicMock()
        addr_mock = MagicMock()
        input_values = ['Jan', 'Novák', 'jan.novak@gmail.com', 'jnovak', 'password']
        output_values = ['Autor vytvořen', 'Done']
        expected_calls = [
            call("Napište křestní jméno autora: ", conn_mock, addr_mock),
            call("Napište příjmení autora: ", conn_mock, addr_mock),
            call("Napište email autora: ", conn_mock, addr_mock),
            call("Napište přihlašovací jméno autora: ", conn_mock, addr_mock),
            call("Napište heslo autora: ", conn_mock, addr_mock)
        ]

        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            with unittest.mock.patch('builtins.input', side_effect=input_values):
                with unittest.mock.patch('src.send_read_PuTTY.send'):
                    autor_CRUD.create = MagicMock(return_value=None)
                    C_autor(connection_mock, conn_mock, addr_mock)

        autor_CRUD.create.assert_called_once_with(connection_mock, 'Jan', 'Novák', 'jan.novak@gmail.com', 'jnovak',
                                                  'password', '1')
        send_read_PuTTY.send.assert_has_calls([call(output) for output in output_values])
        send_read_PuTTY.send.assert_has_calls(expected_calls)
        self.assertEqual(mock_stdout.getvalue().strip(), '')

    def test_create_autor_error(self):
        connection_mock = MagicMock()
        conn_mock = MagicMock()
        addr_mock = MagicMock()
        input_values = ['Jan', 'Novák', 'jan.novak@gmail.com', 'jnovak', 'password']
        error_message = 'Error: AC003'
        expected_calls = [
            call("Napište křestní jméno autora: ", conn_mock, addr_mock),
            call("Napište příjmení autora: ", conn_mock, addr_mock),
            call("Napište email autora: ", conn_mock, addr_mock),
            call("Napište přihlašovací jméno autora: ", conn_mock, addr_mock),
            call("Napište heslo autora: ", conn_mock, addr_mock)
        ]

        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            with unittest.mock.patch('builtins.input', side_effect=input_values):
                with unittest.mock.patch('src.send_read_PuTTY.send'):
                    autor_CRUD.create = MagicMock(side_effect=Exception(error_message))
                    C_autor(connection_mock, conn_mock, addr_mock)

        autor_CRUD.create.assert_called_once_with(connection_mock, 'Jan', 'Novák', 'jan.novak@gmail.com', 'jnovak',
                                                  'password', '1')
        send_read_PuTTY.send.assert_called_with(error_message, conn_mock, addr_mock)
        send_read_PuTTY.send.assert_has_calls(expected_calls)
        self.assertEqual(mock_stdout.getvalue().strip(), '')


class TestAutorCRUD(unittest.TestCase):

    def setUp(self):
        self.connection = sqlite3.connect('test.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            'CREATE TABLE autor (id INTEGER PRIMARY KEY, jmeno TEXT, prijmeni TEXT, email TEXT, prihlasovaci_jmeno TEXT, heslo TEXT, opravneni TEXT)')
        self.connection.commit()

    def tearDown(self):
        self.cursor.execute('DROP TABLE IF EXISTS autor')
        self.connection.commit()
        self.connection.close()

    def test_create_autor(self):
        autor_CRUD.create(self.connection, 'Jan', 'Novák', 'jan.novak@email.com',
                          'jannovak', 'heslo123', '1')
        self.cursor.execute('SELECT * FROM autor')
        rows = self.cursor.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][1], 'Jan')
        self.assertEqual(rows[0][2], 'Novák')
        self.assertEqual(rows[0][3], 'jan.novak@email.com')
        self.assertEqual(rows[0][4], 'jannovak')
        self.assertEqual(rows[0][5], 'heslo123')
        self.assertEqual(rows[0][6], '1')

    def test_read_autor(self):
        self.cursor.execute(
            "INSERT INTO autor (jmeno, prijmeni, email, prihlasovaci_jmeno, heslo, opravneni) VALUES ('Jan', 'Novák', 'jan.novak@email.com', 'jannovak', 'heslo123', '1')")
        self.connection.commit()
        result = autor_CRUD.read(self.connection)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 'Jan')
        self.assertEqual(result[0][2], 'Novák')
        self.assertEqual(result[0][3], 'jan.novak@email.com')
        self.assertEqual(result[0][4], 'jannovak')
        self.assertEqual(result[0][5], 'heslo123')
        self.assertEqual(result[0][6], '1')

    def test_delete_autor(self):
        self.cursor.execute(
            "INSERT INTO autor (jmeno, prijmeni, email, prihlasovaci_jmeno, heslo, opravneni) VALUES ('Jan', 'Novák', 'jan.novak@email.com', 'jannovak', 'heslo123', '1')")
        self.connection.commit()
        autor_CRUD.delete(self.connection, 1)
        self.cursor.execute('SELECT * FROM autor')
        rows = self.cursor.fetchall()
        self.assertEqual(len(rows), 0)