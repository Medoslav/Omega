import unittest
from SERVER.DB_client.pripojeni_db import start_DB
from SERVER.DB_client.CRUD import autor_CRUD
from SERVER.DB_client.CRUD import admin_CRUD
from SERVER.DB_client.CRUD import clanek_CRUD
from SERVER.DB_client.CRUD import komentar_CRUD
from SERVER.DB_client.CRUD import zabanovana_slova_CRUD

class autor_CRUD(unittest.TestCase):
    def test_create(self):
        # připojení k databázi
        connection = start_DB("localhost","omega_admin","123")

        # vložení testovacího řádku do tabulky autor
        autor_CRUD.create(connection, "Test", "Testovací", "test@test.cz", "testovaci", "test123", "0")

        # volání funkce read
        result = autor_CRUD.read(connection)

        # ověření, zda je návratová hodnota list
        self.assertIsInstance(result, list)

        # ověření, zda testovací řádek je v návratové hodnotě
        self.assertIn((1,"Test", "Testovací", "test@test.cz", "testovaci", "test123", "0"), result)

        # vymazání testovacího řádku z tabulky autor
        autor_CRUD.delete(connection, "1")

        # uzavření spojení s databází
        connection.close()


class admin_CRUD(unittest.TestCase):
    def test_create(self):
        # připojení k databázi
        connection = start_DB("localhost","omega_admin","123")

        # vložení testovacího řádku do tabulky autor
        admin_CRUD.create(connection, "Test", "Testovací", "testovaci", "test123")

        # volání funkce read
        result = admin_CRUD.read(connection)

        # ověření, zda je návratová hodnota list
        self.assertIsInstance(result, list)

        # ověření, zda testovací řádek je v návratové hodnotě
        self.assertIn((1,"Test", "Testovací", "testovaci", "test123"), result)

        # vymazání testovacího řádku z tabulky autor
        admin_CRUD.delete(connection, "1")

        # uzavření spojení s databází
        connection.close()

class clanek_CRUD(unittest.TestCase):
    def test_create(self):
        # připojení k databázi
        connection = start_DB("localhost","omega_admin","123")

        # vložení testovacího řádku do tabulky autor
        clanek_CRUD.create(connection, "1", "Testovací", "1999-02-22")

        # volání funkce read
        result = clanek_CRUD.read(connection)

        # ověření, zda je návratová hodnota list
        self.assertIsInstance(result, list)

        # ověření, zda testovací řádek je v návratové hodnotě
        self.assertIn((1 ,1, "Testovací", "1999-02-22"), result)

        # vymazání testovacího řádku z tabulky autor
        clanek_CRUD.delete(connection, "1")

        # uzavření spojení s databází
        connection.close()

class komentar_CRUD(unittest.TestCase):
    def test_create(self):
        # připojení k databázi
        connection = start_DB("localhost","omega_admin","123")

        # vložení testovacího řádku do tabulky autor
        komentar_CRUD.create(connection, "1", "1","Test", "1999-02-22")

        # volání funkce read
        result = komentar_CRUD.read(connection)

        # ověření, zda je návratová hodnota list
        self.assertIsInstance(result, list)

        # ověření, zda testovací řádek je v návratové hodnotě
        self.assertIn((1, 1, 1,"Test", "1999-02-22"), result)

        # vymazání testovacího řádku z tabulky autor
        komentar_CRUD.delete(connection, "1")

        # uzavření spojení s databází
        connection.close()

class slovo_CRUD(unittest.TestCase):
    def test_create(self):
        # připojení k databázi
        connection = start_DB("localhost","omega_admin","123")

        # vložení testovacího řádku do tabulky autor
        zabanovana_slova_CRUD.create(connection, "Test")

        # volání funkce read
        result = zabanovana_slova_CRUD.read(connection)

        # ověření, zda je návratová hodnota list
        self.assertIsInstance(result, list)

        # ověření, zda testovací řádek je v návratové hodnotě
        self.assertIn((18,"Test"), result)

        # vymazání testovacího řádku z tabulky autor
        zabanovana_slova_CRUD.delete(connection, "18")

        # uzavření spojení s databází
        connection.close()