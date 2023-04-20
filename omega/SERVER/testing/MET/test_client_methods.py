import sqlite3
import unittest
import mysql.connector
from unittest.mock import patch, Mock
from datetime import datetime

from SERVER import main
from SERVER.DB_client.DB_methods.DB_admin_metody import admin_login, ban_user_name, unban_user_name
from SERVER.DB_client.pripojeni_db import start_DB, connection
from SERVER.DB_client.DB_methods.DB_user_metody import client_login, client_clan_dat, client_clan_text, \
    client_komentar_id, client_komentar_dat
from SERVER.DB_client.DB_methods.DB_user_metody import client_reg_jm
from SERVER.DB_client.DB_methods.DB_user_metody import client_reg_em
from SERVER.DB_client.DB_methods.DB_user_metody import client_clan_id
from SERVER.DB_client.DB_methods.DB_user_metody import client_aut_pr
from SERVER.DB_client.DB_methods.DB_user_metody import client_clanek_date

class TestClientLogin(unittest.TestCase):

    def setUp(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='omega'
        )

    def tearDown(self):
        self.connection.close()

    def test_valid_login(self):
        # Test a valid login
        username = 'testuser'
        expected_password = 'testpassword'
        actual_password = client_login(self.connection, username)
        self.assertEqual(actual_password, expected_password)

    def test_invalid_login(self):
        # Test an invalid login
        username = 'nonexistentuser'
        expected_password = ' '
        actual_password = client_login(self.connection, username)
        self.assertEqual(actual_password, expected_password)


class TestClientRegJm(unittest.TestCase):

    # Test if the function returns "Y" when the username is not in the database
    def test_valid_username(self):
        with patch('mysql.connector.connect') as mock_connect:
            with patch('mysql.connector.cursor') as mock_cursor:
                mock_cursor.return_value.fetchone.return_value = None
                result = client_reg_jm(mock_connect, "john_doe")
                self.assertEqual(result, "Y")

    # Test if the function returns "N1" when the username is already in the database
    def test_invalid_username(self):
        with patch('mysql.connector.connect') as mock_connect:
            with patch('mysql.connector.cursor') as mock_cursor:
                mock_cursor.return_value.fetchone.return_value = ("john_doe",)
                result = client_reg_jm(mock_connect, "john_doe")
                self.assertEqual(result, "N1")

class TestClientRegEm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a database connection for testing
        cls.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="test_db"
        )

    @classmethod
    def tearDownClass(cls):
        # close the database connection
        cls.connection.close()

    def test_new_email(self):
        # test registering with a new email
        result = client_reg_em(self.connection, "test@example.com")
        self.assertEqual(result, "Y")

    def test_existing_email(self):
        # test registering with an existing email
        result = client_reg_em(self.connection, "existing@example.com")
        self.assertEqual(result, "N1")

class TestClientClanId(unittest.TestCase):
    class TestClientClanId(unittest.TestCase):
        def setUp(self):
            # Establish a connection to a test database
            self.connection = mysql.connector.connect(
                host="localhost",
                user="testuser",
                password="testpassword",
                database="testdb"
            )

        def tearDown(self):
            # Close the connection
            self.connection.close()

        def test_client_clan_id(self):
            # Call the function and check if the returned value is a string
            result = client_clan_id(self.connection)
            self.assertIsInstance(result, str)

class TestClientAutPr(unittest.TestCase):

    def setUp(self):
        # Establish a connection to the database
        self.connection = mysql.connector.connect(
            host="your_host",
            user="your_user",
            password="your_password",
            database="your_database"
        )

    def test_client_aut_pr(self):
        # Test the function with a known article ID
        id = "1"
        expected_result = "JohnDoe"  # Replace with the expected author's username
        result = client_aut_pr(self.connection, id)
        self.assertEqual(result, expected_result)

    def tearDown(self):
        # Close the connection to the database
        self.connection.close()


class TestClientClanDat(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up a test database connection
        cls.connection = start_DB("localhost", "test_user", "test_password")
        # Create a test table and insert a row with a known date
        cursor = cls.connection.cursor()
        cursor.execute("""
            CREATE TABLE clanek (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nazev_clanku VARCHAR(255) NOT NULL,
                obsah_clanku TEXT NOT NULL,
                autor_id INT NOT NULL,
                datum_clanku DATE NOT NULL
            );
        """)
        cursor.execute("""
            INSERT INTO clanek (nazev_clanku, obsah_clanku, autor_id, datum_clanku)
            VALUES ('Test article', 'This is a test article.', 1, '2022-05-01');
        """)
        cls.connection.commit()

    @classmethod
    def tearDownClass(cls):
        # Clean up the test database connection and table
        cursor = cls.connection.cursor()
        cursor.execute("DROP TABLE clanek;")
        cls.connection.close()

    def test_client_clan_dat(self):
        # Test that the function returns the expected date string
        expected_date = datetime(2022, 5, 1).strftime('%Y-%m-%d')
        result = client_clan_dat(self.connection, '1')
        self.assertEqual(result, expected_date)

class TestClientClanText(unittest.TestCase):

    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE clanek (id INTEGER PRIMARY KEY, text_clanku TEXT)")
        cursor.execute("INSERT INTO clanek (id, text_clanku) VALUES (1, 'Hello world!')")
        self.connection.commit()

    def tearDown(self):
        self.connection.close()

    def test_client_clan_text_exists(self):
        result = client_clan_text(self.connection, 1)
        self.assertIsNotNone(result)

    def test_client_clan_text_returns_text(self):
        result = client_clan_text(self.connection, 1)
        self.assertEqual(result, 'Hello world!')

    def test_client_clan_text_invalid_id(self):
        result = client_clan_text(self.connection, 2)
        self.assertIsNone(result)


class TestDatabaseFunctions(unittest.TestCase):

    def test_admin_login(self):
        # test valid admin username and password
        self.assertEqual(admin_login(connection, "admin1"), "heslo1")

        # test invalid admin username
        self.assertEqual(admin_login(connection, "invalid_username"), " ")

    def test_ban_user_name(self):
        # ban a user
        ban_user_name(connection, "jmeno_autora")

        # check if the user is banned
        cursor = connection.cursor()
        command = "SELECT ban FROM autor WHERE jmeno_autor = 'jmeno_autora';"
        cursor.execute(command)
        for x in cursor:
            ban = x[0]
        self.assertEqual(ban, 1)

    def test_unban_user_name(self):
        # unban a user
        unban_user_name(connection, "jmeno_autora")

        # check if the user is unbanned
        cursor = connection.cursor()
        command = "SELECT ban FROM autor WHERE jmeno_autor = 'jmeno_autora';"
        cursor.execute(command)
        for x in cursor:
            ban = x[0]
        self.assertEqual(ban, 0)

    def test_client_login(self):
        # test valid client username and password
        self.assertEqual(client_login(connection, "prezdivka_autora"), "heslo_autora")

        # test invalid client username
        self.assertEqual(client_login(connection, "invalid_username"), " ")

    def test_client_reg_jm(self):
        # test valid author name that doesn't exist in the database
        self.assertEqual(client_reg_jm(connection, "new_author"), "Y")

        # test invalid author name that already exists in the database
        self.assertEqual(client_reg_jm(connection, "prezdivka_autora"), "N1")

    def test_client_reg_em(self):
        # test valid email that doesn't exist in the database
        self.assertEqual(client_reg_em(connection, "new_email@example.com"), "Y")

        # test invalid email that already exists in the database
        self.assertEqual(client_reg_em(connection, "email_autora@example.com"), "N1")

    def test_client_clan_id(self):
        # test if the function returns an integer
        self.assertIsInstance(int(client_clan_id(connection)), int)

    def test_client_aut_pr(self):
        # test if the function returns a string
        self.assertIsInstance(client_aut_pr(connection, "1"), str)

    def test_client_clan_dat(self):
        # test if the function returns a string
        self.assertIsInstance(client_clan_dat(connection, "1"), str)

    def test_client_clan_text(self):
        # test if the function returns a string
        self.assertIsInstance(client_clan_text(connection, "1"), str)

    def test_client_komentar_id(self):
        # test if the function returns a list
        self.assertIsInstance(client_komentar_id(connection, "1"), list)

class TestClientKomentarPr(unittest.TestCase):

    def test_existing_id(self):
        # Test with existing id
        connection = Mock()
        cursor = Mock()
        cursor.execute.return_value = [(1,)]
        cursor.execute.side_effect = [[(1,)], [("John Doe",)]]
        connection.cursor.return_value = cursor
        result = main.client_komentar_pr(connection, 1)
        self.assertEqual(result, "John Doe")

    def test_nonexisting_id(self):
        # Test with non-existing id
        connection = Mock()
        cursor = Mock()
        cursor.execute.return_value = []
        connection.cursor.return_value = cursor
        result = main.client_komentar_pr(connection, 99)
        self.assertIsNone(result)


class TestClientKomentarDat(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.conn = sqlite3.connect("my_database.db")
        cls.cursor = cls.conn.cursor()
        cls.cursor.execute(
            "CREATE TABLE IF NOT EXISTS autor (id INTEGER PRIMARY KEY, prezdivka_autor TEXT, heslo_autor TEXT, email_autor TEXT, ban INTEGER);")
        cls.cursor.execute(
            "CREATE TABLE IF NOT EXISTS clanek (id INTEGER PRIMARY KEY, nazev_clanku TEXT, text_clanku TEXT, autor_id INTEGER, datum_clanku DATE);")
        cls.cursor.execute(
            "CREATE TABLE IF NOT EXISTS komentar (id INTEGER PRIMARY KEY, text_komentare TEXT, autor_id INTEGER, clanek_id INTEGER, datum_komentare DATE);")
        cls.conn.commit()

    @classmethod
    def tearDownClass(cls):
        cls.cursor.execute("DROP TABLE IF EXISTS komentar;")
        cls.cursor.execute("DROP TABLE IF EXISTS clanek;")
        cls.cursor.execute("DROP TABLE IF EXISTS autor;")
        cls.conn.commit()
        cls.conn.close()

    def setUp(self):
        self.cursor.execute("INSERT INTO autor (prezdivka_autor, heslo_autor, email_autor, ban) VALUES (?, ?, ?, ?);",
                            ("test_user", "password123", "test_user@example.com", 0))
        self.cursor.execute(
            "INSERT INTO clanek (nazev_clanku, text_clanku, autor_id, datum_clanku) VALUES (?, ?, ?, ?);",
            ("Test Article", "This is a test article.", 1, "2023-04-18"))
        self.cursor.execute(
            "INSERT INTO komentar (text_komentare, autor_id, clanek_id, datum_komentare) VALUES (?, ?, ?, ?);",
            ("This is a test comment.", 1, 1, "2023-04-18"))
        self.conn.commit()

    def tearDown(self):
        self.cursor.execute("DELETE FROM komentar;")
        self.cursor.execute("DELETE FROM clanek;")
        self.cursor.execute("DELETE FROM autor;")
        self.conn.commit()

    def test_client_komentar_dat(self):
        expected_output = "2023-04-18"
        actual_output = client_komentar_dat(self.conn, 1)
        self.assertEqual(actual_output, expected_output)

