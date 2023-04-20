import sqlite3
import unittest
from datetime import datetime
from email import message
from io import StringIO
from unittest.mock import patch, MagicMock, Mock

from CLIENT import main
from SERVER.DB_client.DB_methods import DB_user_metody
from SERVER.PuTTY_server import send_read_PuTTY
from SERVER.client.client_commands import log, reg, gcl, kom
from SERVER.testing.test_CRUD_autor import autor_CRUD


class TestLogFunction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up a connection to an in-memory database for testing
        cls.connection = sqlite3.connect(":memory:")
        DB_user_metody.create_table(cls.connection)

    @classmethod
    def tearDownClass(cls):
        # Close the connection and clean up the database
        cls.connection.close()

    def setUp(self):
        # Set up a fake client connection and address for testing
        self.conn = "fake_conn"
        self.addr = "fake_addr"

    def test_successful_login(self):
        # Test a successful login
        DB_user_metody.create(self.connection, "TestUser", "TestPassword")
        send_read_PuTTY.send = lambda message, conn, addr: None
        send_read_PuTTY.read = lambda conn, addr: "TestUser" if message == "Y" else "TestPassword"
        result = log(self.conn, self.addr, self.connection)
        expected = "Y"
        self.assertEqual(result, expected)

    def test_failed_login(self):
        # Test a failed login with incorrect password
        DB_user_metody.create(self.connection, "TestUser", "TestPassword")
        send_read_PuTTY.send = lambda message, conn, addr: None
        send_read_PuTTY.read = lambda conn, addr: "TestUser" if message == "Y" else "WrongPassword"
        result = log(self.conn, self.addr, self.connection)
        expected = "N"
        self.assertEqual(result, expected)

    def test_banned_user(self):
        # Test a login attempt by a banned user
        DB_user_metody.create(self.connection, "BannedUser", "TestPassword", banned=True)
        send_read_PuTTY.send = lambda message, conn, addr: None
        send_read_PuTTY.read = lambda conn, addr: "BannedUser" if message == "Y" else "TestPassword"
        result = log(self.conn, self.addr, self.connection)
        expected = "Ban"
        self.assertEqual(result, expected)


class TestReg(unittest.TestCase):

    @patch('send_read_PuTTY.send')
    @patch('send_read_PuTTY.read')
    @patch('DB_user_metody.client_reg_jm')
    @patch('DB_user_metody.client_reg_em')
    @patch('autor_CRUD.create')
    def test_reg_success(self, mock_create, mock_reg_em, mock_reg_jm, mock_read, mock_send):
        mock_read.side_effect = ['jmeno', 'prijmeni', 'email@example.com', 'prezdivka', 'heslo']
        mock_reg_jm.return_value = 'Y'
        mock_reg_em.return_value = 'Y'

        self.assertEqual(reg(None, None, None), 'Y')
        mock_send.assert_called_with('Y', None, None)
        mock_create.assert_called_with(None, 'jmeno', 'prijmeni', 'email@example.com', 'prezdivka', 'heslo', '0')

    @patch('send_read_PuTTY.send')
    @patch('send_read_PuTTY.read')
    @patch('DB_user_metody.client_reg_jm')
    @patch('DB_user_metody.client_reg_em')
    @patch('autor_CRUD.create')
    def test_reg_invalid_email(self, mock_create, mock_reg_em, mock_reg_jm, mock_read, mock_send):
        mock_read.side_effect = ['jmeno', 'prijmeni', 'invalid_email', 'prezdivka', 'heslo']
        mock_reg_jm.return_value = 'Y'
        mock_reg_em.return_value = 'Y'

        self.assertEqual(reg(None, None, None), 'N2')
        mock_send.assert_called_with('N2', None, None)
        mock_create.assert_not_called()

    @patch('send_read_PuTTY.send')
    @patch('send_read_PuTTY.read')
    @patch('DB_user_metody.client_reg_jm')
    @patch('DB_user_metody.client_reg_em')
    @patch('autor_CRUD.create')
    def test_reg_duplicate_email(self, mock_create, mock_reg_em, mock_reg_jm, mock_read, mock_send):
        mock_read.side_effect = ['jmeno', 'prijmeni', 'email@example.com', 'prezdivka', 'heslo']
        mock_reg_jm.return_value = 'Y'
        mock_reg_em.return_value = 'N1'

        self.assertEqual(reg(None, None, None), 'N1')
        mock_send.assert_called_with('N1', None, None)
        mock_create.assert_not_called()

    @patch('send_read_PuTTY.send')
    @patch('send_read_PuTTY.read')
    @patch('DB_user_metody.client_reg_jm')
    @patch('DB_user_metody.client_reg_em')
    @patch('autor_CRUD.create')
    def test_reg_duplicate_jmeno(self, mock_create, mock_reg_em, mock_reg_jm, mock_read, mock_send):
        mock_read.side_effect = ['jmeno', 'prijmeni', 'email@example.com', 'prezdivka', 'heslo']
        mock_reg_jm.return_value = 'N1'

        self.assertEqual(reg(None, None, None), 'N1')
        mock_send.assert_called_with('N1', None, None)
        mock_create.assert_not_called()

class TestGcl(unittest.TestCase):

    def setUp(self):
        self.connection = sqlite3.connect(':memory:')
        with self.connection:
            self.connection.execute('''
                CREATE TABLE autor (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    jmeno VARCHAR(50) NOT NULL,
                    prijmeni VARCHAR(50) NOT NULL,
                    email VARCHAR(50) NOT NULL UNIQUE,
                    prezdivka VARCHAR(50) NOT NULL UNIQUE,
                    heslo VARCHAR(255) NOT NULL,
                    admin VARCHAR(1) NOT NULL
                )
            ''')

            self.connection.execute('''
                CREATE TABLE clanek (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    autor_id INTEGER NOT NULL,
                    datum DATE NOT NULL,
                    text TEXT NOT NULL,
                    FOREIGN KEY (autor_id) REFERENCES autor (id)
                )
            ''')

            autor_CRUD.create(self.connection, "Test", "Testovac", "test@test.com", "testik", "test", "0")
            self.connection.execute('''
                INSERT INTO clanek (autor_id, datum, text)
                VALUES (?, ?, ?)
            ''', (1, '2023-04-18', 'Toto je testovací článek'))

        self.conn = MagicMock()
        self.addr = MagicMock()

    def test_gcl(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.conn.recv.return_value = b'Y'
            self.assertEqual(gcl.gcl(self.conn, self.addr, self.connection), None)
            self.conn.send.assert_called_with(b'Test Testovac')
            self.conn.send.assert_called_with(b'2023-04-18')
            self.conn.send.assert_called_with(b'Toto je testovací článek')
            self.conn.send.assert_called_with(b'1')

    def tearDown(self):
        self.connection.close()

class TestCla(unittest.TestCase):

    def test_new_article_added_to_database(self):
        conn = Mock()
        addr = Mock()
        connection = Mock()
        jmeno = 'test_author'
        text = 'test article text'
        with patch.object(DB_user_metody, 'client_clanek_duplik', return_value='Y'):
            with patch.object(DB_user_metody, 'client_clanek_userid', return_value=123):
                with patch.object(DB_user_metody, 'client_clanek_date', return_value=datetime.now()):
                    with patch.object(DB_user_metody, 'client_clanek_imp') as mock_client_clanek_imp:
                        result = main.cla(conn, addr, connection, jmeno, text)
                        self.assertEqual(result, 'Y')
                        mock_client_clanek_imp.assert_called_with(connection, '123', 'test article text', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def test_article_already_exists(self):
        conn = Mock()
        addr = Mock()
        connection = Mock()
        jmeno = 'test_author'
        text = 'test article text'
        with patch.object(DB_user_metody, 'client_clanek_duplik', return_value='N'):
            result = main.cla(conn, addr, connection, jmeno, text)
            self.assertEqual(result, 'N')


class TestKom(unittest.TestCase):

    def setUp(self):
        self.conn = None
        self.addr = None
        self.connection = None

    def test_kom_with_valid_inputs(self):
        # Mock the send and read functions to simulate user input
        send_read_PuTTY.send = lambda msg, conn, addr: None
        send_read_PuTTY.read = lambda conn, addr: None

        # Mock the client_clanek_userid and client_clanek_date functions to simulate database response
        DB_user_metody.client_clanek_userid = lambda conn, jmeno: 1
        DB_user_metody.client_clanek_date = lambda: datetime.datetime.now()

        # Test with valid inputs
        self.assertEqual(kom(self.conn, self.addr, self.connection), "Y")

    def test_kom_with_duplicate_comment(self):
        # Mock the send and read functions to simulate user input
        send_read_PuTTY.send = lambda msg, conn, addr: None
        send_read_PuTTY.read = lambda conn, addr: None

        # Mock the client_komentar_duplik function to simulate database response
        DB_user_metody.client_komentar_duplik = lambda conn, cl_id, text: "N"

        # Test with duplicate comment
        self.assertEqual(kom(self.conn, self.addr, self.connection), "N")


