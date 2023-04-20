import unittest
import mysql.connector
from SERVER.DB_client.DB_methods.DB_admin_metody import admin_login
from SERVER.DB_client.DB_methods.DB_admin_metody import ban_user_name


class TestAdminLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="omega"
        )

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()

    def test_admin_login_valid_username(self):
        # Test valid username
        result = admin_login(self.connection, "admin")
        self.assertEqual(result, "password")

    def test_admin_login_invalid_username(self):
        # Test invalid username
        result = admin_login(self.connection, "nonexistent_admin")
        self.assertEqual(result, " ")


class TestBanUserName(unittest.TestCase):

    # nastavení testovacího prostředí
    def setUp(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="testuser",
            password="testpassword",
            database="testdb"
        )
        self.cursor = self.connection.cursor()
        # vytvoření testovací tabulky
        self.cursor.execute("""
            CREATE TABLE autor (
                jmeno_autor VARCHAR(255) NOT NULL PRIMARY KEY,
                prijmeni_autor VARCHAR(255) NOT NULL,
                email_autor VARCHAR(255) NOT NULL,
                prezdivka_autor VARCHAR(255) NOT NULL,
                heslo_autor VARCHAR(255) NOT NULL,
                ban BOOLEAN NOT NULL
            );
        """)
        self.connection.commit()

    # ukončení testovacího prostředí
    def tearDown(self):
        self.cursor.execute("DROP TABLE autor;")
        self.connection.commit()
        self.connection.close()

    # test banování uživatele
    def test_ban_user_name(self):
        # vložení testovacího uživatele do tabulky autor
        self.cursor.execute(
            "INSERT INTO autor (jmeno_autor, prijmeni_autor, email_autor, prezdivka_autor, heslo_autor, ban) VALUES ('Testovaci', 'Uzivatel', 'testovaci.uzivatel@test.com', 'testovaci', 'testheslo', 0);")
        self.connection.commit()

        # otestování funkce ban_user_name
        ban_user_name(self.connection, 'Testovaci')
        self.cursor.execute("SELECT ban FROM autor WHERE jmeno_autor = 'Testovaci';")
        result = self.cursor.fetchone()
        self.assertEqual(result[0], True)

class TestUnanUserName(unittest.TestCase):

    # nastavení testovacího prostředí
    def setUp(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="testuser",
            password="testpassword",
            database="testdb"
        )
        self.cursor = self.connection.cursor()
        # vytvoření testovací tabulky
        self.cursor.execute("""
            CREATE TABLE autor (
                jmeno_autor VARCHAR(255) NOT NULL PRIMARY KEY,
                prijmeni_autor VARCHAR(255) NOT NULL,
                email_autor VARCHAR(255) NOT NULL,
                prezdivka_autor VARCHAR(255) NOT NULL,
                heslo_autor VARCHAR(255) NOT NULL,
                ban BOOLEAN NOT NULL
            );
        """)
        self.connection.commit()

    # ukončení testovacího prostředí
    def tearDown(self):
        self.cursor.execute("DROP TABLE autor;")
        self.connection.commit()
        self.connection.close()

    # test banování uživatele
    def test_ban_user_name(self):
        # vložení testovacího uživatele do tabulky autor
        self.cursor.execute(
            "INSERT INTO autor (jmeno_autor, prijmeni_autor, email_autor, prezdivka_autor, heslo_autor, ban) VALUES ('Testovaci', 'Uzivatel', 'testovaci.uzivatel@test.com', 'testovaci', 'testheslo', 0);")
        self.connection.commit()

        # otestování funkce ban_user_name
        ban_user_name(self.connection, 'Testovaci')
        self.cursor.execute("SELECT ban FROM autor WHERE jmeno_autor = 'Testovaci';")
        result = self.cursor.fetchone()
        self.assertEqual(result[0], True)

