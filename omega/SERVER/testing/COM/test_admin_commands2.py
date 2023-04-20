import io
import sqlite3
import unittest
from unittest.mock import MagicMock, patch, call, Mock

from SERVER.DB_client.CRUD import admin_CRUD, autor_CRUD, zabanovana_slova_CRUD
from SERVER.PuTTY_server import send_read_PuTTY
from SERVER.admin.admin_commands1 import C_admin, R_admin, D_admin, C_autor, D_autor, C_ban, R_ban, U_autor, R_autor


class TestU_autor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect("databaze.db")

    def test_update_existing_column(self):
        conn, addr = None, None
        autor_CRUD.create(self.connection, "Test", "Testovski", "test@test.com", "testovac", "testheslo", "1")
        autor_CRUD.create(self.connection, "Test2", "Testovski2", "test2@test.com", "testovac2", "testheslo2", "1")
        send_read_PuTTY.read = lambda conn, addr: "1"
        send_read_PuTTY.send = lambda msg, conn, addr: None
        autor_CRUD.read = lambda conn: [("1", "Test", "Testovski", "test@test.com", "testovac", "testheslo", "1"),
                                        ("2", "Test2", "Testovski2", "test2@test.com", "testovac2", "testheslo2", "1")]
        send_read_PuTTY.read = lambda conn, addr: "jmeno"
        send_read_PuTTY.read = lambda conn, addr: "1"
        send_read_PuTTY.read = lambda conn, addr: "Test3"
        autor_CRUD.update(self.connection, "jmeno", "1", "Test3")
        updated_record = autor_CRUD.read(self.connection, "1")
        self.assertEqual(updated_record[1], "Test3")

    def test_update_non_existing_column(self):
        conn, addr = None, None
        autor_CRUD.create(self.connection, "Test", "Testovski", "test@test.com", "testovac", "testheslo", "1")
        send_read_PuTTY.read = lambda conn, addr: "1"
        send_read_PuTTY.send = lambda msg, conn, addr: None
        autor_CRUD.read = lambda conn: [("1", "Test", "Testovski", "test@test.com", "testovac", "testheslo", "1")]
        send_read_PuTTY.read = lambda conn, addr: "nonexistingcolumn"
        autor_CRUD.update(self.connection, "nonexistingcolumn", "1", "newvalue")
        updated_record = autor_CRUD.read(self.connection, "1")
        self.assertNotEqual(updated_record[1], "newvalue")

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()


class TestDAutor(unittest.TestCase):

    def setUp(self):
        self.connection = sqlite3.connect("test.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS autor (id INTEGER PRIMARY KEY, jmeno TEXT, prijmeni TEXT, email TEXT, prihlasovaci_jmeno TEXT, heslo TEXT, admin TEXT)")
        self.connection.commit()

    def test_delete_autor(self):
        # Insert a new autor into the table
        self.cursor.execute(
            "INSERT INTO autor (jmeno, prijmeni, email, prihlasovaci_jmeno, heslo, admin) VALUES (?, ?, ?, ?, ?, ?)",
            ('Test', 'Autor', 'test@test.com', 'test_autor', 'password', '0'))
        self.connection.commit()
        # Get the id of the autor that was just inserted
        self.cursor.execute("SELECT id FROM autor WHERE prihlasovaci_jmeno=?", ('test_autor',))
        result = self.cursor.fetchone()
        autor_id = result[0]
        # Call the D_autor function with the autor_id
        D_autor(self.connection, self.conn, self.addr)
        # Check if the autor was successfully deleted
        self.cursor.execute("SELECT id FROM autor WHERE id=?", (autor_id,))
        result = self.cursor.fetchone()
        self.assertIsNone(result)

    def tearDown(self):
        self.connection.close()

class TestCreateBan(unittest.TestCase):

    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        zabanovana_slova_CRUD.create_table(self.connection)
        self.conn = Mock()
        self.addr = Mock()

    def test_create_ban_successful(self):
        with patch('builtins.input', side_effect=['test_slovo']):
            with patch('sys.stdout', new=io.StringIO()) as fakeOutput:
                C_ban(self.connection, self.conn, self.addr)
                self.assertIn("Zabanovane slovo vytvoreno", fakeOutput.getvalue())

        result = zabanovana_slova_CRUD.read(self.connection)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], "test_slovo")

    def test_create_ban_error(self):
        with patch('builtins.input', side_effect=['test_slovo']):
            zabanovana_slova_CRUD.create(self.connection, "test_slovo")

        with patch('builtins.input', side_effect=['test_slovo']):
            with patch('sys.stdout', new=io.StringIO()) as fakeOutput:
                C_ban(self.connection, self.conn, self.addr)
                self.assertIn("Error:", fakeOutput.getvalue())

        result = zabanovana_slova_CRUD.read(self.connection)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], "test_slovo")

    def tearDown(self):
        self.connection.close()

class TestRBan(unittest.TestCase):
    @patch('builtins.print')
    def test_read_banned_words(self, mock_print):
        connection = Mock()
        conn = Mock()
        addr = Mock()

        banned_words = [('word1',), ('word2',), ('word3',)]
        zabanovana_slova_CRUD.read = Mock(return_value=banned_words)

        R_ban(connection, conn, addr)

        zabanovana_slova_CRUD.read.assert_called_once_with(connection)
        mock_print.assert_called_with("[('word1',), ('word2',), ('word3',)]")


class TestCRUDFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up a connection to an in-memory database for testing
        cls.connection = sqlite3.connect(":memory:")
        autor_CRUD.create_table(cls.connection)
        zabanovana_slova_CRUD.create_table(cls.connection)

    @classmethod
    def tearDownClass(cls):
        # Close the connection and clean up the database
        cls.connection.close()

    def setUp(self):
        # Set up a fake client connection and address for testing
        self.conn = "fake_conn"
        self.addr = "fake_addr"

    def test_C_autor(self):
        # Test creating a new author
        send_read_PuTTY.read = lambda conn, addr: "Test Autor"
        C_autor(self.connection, self.conn, self.addr)
        result = autor_CRUD.read(self.connection)
        expected = [(1, "Test Autor")]
        self.assertEqual(result, expected)

    def test_R_autor(self):
        # Test reading all authors
        autor_CRUD.create(self.connection, "Test Autor")
        send_read_PuTTY.send = lambda message, conn, addr: None
        send_read_PuTTY.read = lambda conn, addr: None
        result = []
        send_read_PuTTY.send = lambda message, conn, addr: result.append(message)
        R_autor(self.connection, self.conn, self.addr)
        expected = ["(1, 'Test Autor')", "Done"]
        self.assertEqual(result, expected)

    def test_U_autor(self):
        # Test updating an author
        autor_CRUD.create(self.connection, "Test Autor")
        send_read_PuTTY.read = lambda conn, addr: "autor_name"
        send_read_PuTTY.send = lambda message, conn, addr: None
        U_autor(self.connection, self.conn, self.addr)
        result = autor_CRUD.read(self.connection)
        expected = [(1, "autor_name")]
        self.assertEqual(result, expected)

    def test_D_autor(self):
        # Test deleting an author
        autor_CRUD.create(self.connection, "Test Autor")
        send_read_PuTTY.read = lambda conn, addr: None
        send_read_PuTTY.send = lambda message, conn, addr: None
        D_autor(self.connection, self.conn, self.addr)
        result = autor_CRUD.read(self.connection)
        expected = []
        self.assertEqual(result, expected)

    def test_C_ban(self):
        # Test creating a new banned word
        send_read_PuTTY.read = lambda conn, addr: "Test Ban"
        C_ban(self.connection, self.conn, self.addr)
        result = zabanovana_slova_CRUD.read(self.connection)
        expected = [(1, "Test Ban")]
        self.assertEqual(result, expected)



