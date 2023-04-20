import sqlite3
import unittest
import mysql.connector
from unittest.mock import patch, Mock
from datetime import datetime, date

from SERVER import main
from SERVER.DB_client.DB_methods.DB_admin_metody import admin_login, ban_user_name, unban_user_name
from SERVER.DB_client.pripojeni_db import start_DB, connection
from SERVER.DB_client.DB_methods.DB_user_metody import client_login, client_clan_dat, client_clan_text, \
    client_komentar_id, client_komentar_dat, client_komentar_text, client_clanek_userid, client_clanek_duplik, \
    client_komentar_duplik, client_ban_check
from SERVER.DB_client.DB_methods.DB_user_metody import client_reg_jm
from SERVER.DB_client.DB_methods.DB_user_metody import client_reg_em
from SERVER.DB_client.DB_methods.DB_user_metody import client_clan_id
from SERVER.DB_client.DB_methods.DB_user_metody import client_aut_pr
from SERVER.DB_client.DB_methods.DB_user_metody import client_clanek_date


class TestClientKomentarText(unittest.TestCase):

    def setUp(self):
        # Connect to a temporary in-memory database for testing purposes
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()
        # Create a temporary table and insert some test data
        self.cursor.execute("CREATE TABLE komentar (id INTEGER, text_komenatre TEXT)")
        self.cursor.execute("INSERT INTO komentar VALUES (1, 'Test comment 1')")
        self.cursor.execute("INSERT INTO komentar VALUES (2, 'Test comment 2')")
        self.cursor.execute("INSERT INTO komentar VALUES (3, 'Test comment 3')")

    def test_existing_id(self):
        # Test that the function returns the correct text for an existing comment ID
        result = client_komentar_text(self.connection, 2)
        self.assertEqual(result, "Test comment 2")

    def test_nonexistent_id(self):
        # Test that the function returns None for a nonexistent comment ID
        result = client_komentar_text(self.connection, 4)
        self.assertIsNone(result)

    def tearDown(self):
        # Close the database connection and delete the temporary table
        self.connection.close()

class TestClientClanekUserid(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE autor (id INTEGER PRIMARY KEY, prezdivka_autor TEXT)")
        self.cur.execute("INSERT INTO autor (prezdivka_autor) VALUES ('user1')")
        self.conn.commit()

    def test_existing_user(self):
        self.assertEqual(client_clanek_userid(self.conn, 'user1'), 1)

    def test_non_existing_user(self):
        self.assertEqual(client_clanek_userid(self.conn, 'user2'), None)

    def tearDown(self):
        self.conn.close()

class TestClientFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect("test.db")
        cursor = cls.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS autor (id INTEGER PRIMARY KEY AUTOINCREMENT, jmeno_autor TEXT, email_autor TEXT, prezdivka_autor TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS clanek (id INTEGER PRIMARY KEY AUTOINCREMENT, autor_id INTEGER, datum_clanku TEXT, text_clanku TEXT, FOREIGN KEY(autor_id) REFERENCES autor(id))")
        cursor.execute("CREATE TABLE IF NOT EXISTS komentar (id INTEGER PRIMARY KEY AUTOINCREMENT, autor_id INTEGER, clanek_id INTEGER, datum_komentare TEXT, text_komenatre TEXT, FOREIGN KEY(autor_id) REFERENCES autor(id), FOREIGN KEY(clanek_id) REFERENCES clanek(id))")
        cls.connection.commit()

    def test_client_reg_em(self):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO autor(jmeno_autor, email_autor, prezdivka_autor) VALUES('Jan Novak', 'jan.novak@example.com', 'jannovak')")
        self.assertEqual(client_reg_em(self.connection, 'jan.novak@example.com'), 'N1')
        self.assertEqual(client_reg_em(self.connection, 'petr.novak@example.com'), 'Y')
        cursor.execute("DELETE FROM autor")
        self.connection.commit()

    def test_client_clan_id(self):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO clanek(autor_id, datum_clanku, text_clanku) VALUES(1, '2022-01-01', 'Prvni clanek')")
        cursor.execute("INSERT INTO clanek(autor_id, datum_clanku, text_clanku) VALUES(1, '2022-01-02', 'Druhy clanek')")
        cursor.execute("INSERT INTO clanek(autor_id, datum_clanku, text_clanku) VALUES(1, '2022-01-03', 'Treti clanek')")
        self.assertIn(int(client_clan_id(self.connection)), [1, 2, 3])
        cursor.execute("DELETE FROM clanek")
        self.connection.commit()

    def test_client_aut_pr(self):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO autor(jmeno_autor, email_autor, prezdivka_autor) VALUES('Jan Novak', 'jan.novak@example.com', 'jannovak')")
        cursor.execute("INSERT INTO clanek(autor_id, datum_clanku, text_clanku) VALUES(1, '2022-01-01', 'Prvni clanek')")
        self.assertEqual(client_aut_pr(self.connection, '1'), 'jannovak')
        cursor.execute("DELETE FROM clanek")
        cursor.execute("DELETE FROM autor")
        self.connection.commit()

    def test_client_clan_dat(self):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO clanek(autor_id, datum_clanku, text_clanku) VALUES(1, '2022-01-01', 'Prvni clanek')")
        self.assertEqual(client_clan_dat(self.connection, '1'), '2022-01-01')
        cursor.execute("DELETE FROM clanek")
        self.connection.commit()

    def test_client_clan_text(self):
        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO clanek(autor_id, datum_clanku, text_clanku) VALUES(1, '2022-01-01', 'Prvni clanek')")
        self.assertEqual(client_clan_text(self.connection, '1'), 'Prvni clanek')
        cursor.execute("DELETE FROM clanek")
        self.connection.commit()

    def test_client_komentar_dat(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO autor(jmeno_autor, email_autor, prezdivka_autor) VALUES('Jan Novak', 'jan.novak@example.com', 'jannovak')")
        cursor.execute(
            "INSERT INTO clanek(autor_id, datum_clanku, text_clanku) VALUES(1, '2022-01-01', 'Prvni clanek')")
        cursor.execute(
            "INSERT INTO komentar(autor_id, clanek_id, datum_komentare, text_komenatre) VALUES(1, 1, '2022-02-01', 'Komentar k Prvnimu clanku')")
        self.assertEqual(client_komentar_dat(self.connection, '1'), '2022-02-01')
        cursor.execute("DELETE FROM komentar")
        cursor.execute("DELETE FROM clanek")
        cursor.execute("DELETE FROM autor")
        self.connection.commit()

    def test_client_komentar_text(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO autor(jmeno_autor, email_autor, prezdivka_autor) VALUES('Jan Novak', 'jan.novak@example.com', 'jannovak')")
        cursor.execute(
            "INSERT INTO clanek(autor_id, datum_clanku, text_clanku) VALUES(1, '2022-01-01', 'Prvni clanek')")
        cursor.execute(
            "INSERT INTO komentar(autor_id, clanek_id, datum_komentare, text_komenatre) VALUES(1, 1, '2022-02-01', 'Komentar k Prvnimu clanku')")
        self.assertEqual(client_komentar_text(self.connection, '1'), 'Komentar k Prvnimu clanku')
        cursor.execute("DELETE FROM komentar")
        cursor.execute("DELETE FROM clanek")
        cursor.execute("DELETE FROM autor")
        self.connection.commit()

    def test_client_clanek_userid(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO autor(jmeno_autor, email_autor, prezdivka_autor) VALUES('Jan Novak', 'jan.novak@example.com', 'jannovak')")
        self.assertEqual(client_clanek_userid(self.connection, 'jannovak'), 1)
        cursor.execute("DELETE FROM autor")
        self.connection.commit()

    def test_client_clanek_date(self):
        self.assertEqual(client_clanek_date(), date.today().strftime("%Y-%m-%d"))

    def test_client_clanek_duplik(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO clanek(autor_id, datum_clanku, text_clanku) VALUES(1, '2022-01-01', 'Prvni clanek')")
        self.assertEqual(client_clanek_duplik(self.connection, 'Prvni clanek'), 'N')
        self.assertEqual(client_clanek_duplik(self.connection, 'Druhy clanek'), 'Y')
        cursor.execute("DELETE FROM clanek")
        self.connection.commit()

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()

class TestClientFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect("test.db")
        cursor = cls.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS autor (id INTEGER PRIMARY KEY AUTOINCREMENT, jmeno_autor TEXT, email_autor TEXT, prezdivka_autor TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS clanek (id INTEGER PRIMARY KEY AUTOINCREMENT, autor_id INTEGER, datum_clanku TEXT, text_clanku TEXT, FOREIGN KEY(autor_id) REFERENCES autor(id))")
        cursor.execute("CREATE TABLE IF NOT EXISTS komentar (id INTEGER PRIMARY KEY AUTOINCREMENT, autor_id INTEGER, clanek_id INTEGER, datum_komentare TEXT, text_komenatre TEXT, FOREIGN KEY(autor_id) REFERENCES autor(id), FOREIGN KEY(clanek_id) REFERENCES clanek(id))")
        cls.connection.commit()

    def test_client_komentar_duplik(self):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO autor(jmeno_autor, email_autor, prezdivka_autor) VALUES('Jan Novak', 'jan.novak@example.com', 'jannovak')")
        cursor.execute("INSERT INTO clanek(autor_id, datum_clanku, text_clanku) VALUES(1, '2022-01-01', 'Prvni clanek')")
        cursor.execute("INSERT INTO komentar(autor_id, clanek_id, datum_komentare, text_komenatre) VALUES(1, 1, '2022-01-01', 'Komentar k prvnimu clanku')")
        self.assertEqual(client_komentar_duplik(self.connection, '1', 'Komentar k prvnimu clanku'), 'N')
        self.assertEqual(client_komentar_duplik(self.connection, '1', 'Komentar ke druhemu clanku'), 'Y')
        cursor.execute("DELETE FROM komentar")
        cursor.execute("DELETE FROM clanek")
        cursor.execute("DELETE FROM autor")
        self.connection.commit()

class TestClientFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect("test.db")
        cursor = cls.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS autor (id INTEGER PRIMARY KEY AUTOINCREMENT, jmeno_autor TEXT, email_autor TEXT, prezdivka_autor TEXT, ban INTEGER DEFAULT 0)")
        cursor.execute("CREATE TABLE IF NOT EXISTS clanek (id INTEGER PRIMARY KEY AUTOINCREMENT, autor_id INTEGER, datum_clanku TEXT, text_clanku TEXT, FOREIGN KEY(autor_id) REFERENCES autor(id))")
        cursor.execute("CREATE TABLE IF NOT EXISTS komentar (id INTEGER PRIMARY KEY AUTOINCREMENT, autor_id INTEGER, clanek_id INTEGER, datum_komentare TEXT, text_komenatre TEXT, FOREIGN KEY(autor_id) REFERENCES autor(id), FOREIGN KEY(clanek_id) REFERENCES clanek(id))")
        cls.connection.commit()

    def test_client_ban_check(self):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO autor(jmeno_autor, email_autor, prezdivka_autor, ban) VALUES('Jan Novak', 'jan.novak@example.com', 'jannovak', 1)")
        cursor.execute("INSERT INTO autor(jmeno_autor, email_autor, prezdivka_autor, ban) VALUES('Petr Novak', 'petr.novak@example.com', 'petrnovak', 0)")
        self.assertEqual(client_ban_check(self.connection, 'jannovak'), 1)
        self.assertEqual(client_ban_check(self.connection, 'petrnovak'), 0)
        cursor.execute("DELETE FROM autor")
        self.connection.commit()


