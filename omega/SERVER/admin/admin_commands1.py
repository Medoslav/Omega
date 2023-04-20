import time
from SERVER.PuTTY_server import send_read_PuTTY
from SERVER.DB_client.CRUD import admin_CRUD
from SERVER.DB_client.CRUD import autor_CRUD
from SERVER.DB_client.CRUD import zabanovana_slova_CRUD

def C_admin(connection,conn,addr):
    """
    Použivá admin CRUD Create
    :param connection: připojení databáze
    :param conn: připojení clienta
    :param addr: ip clienta
    :return:
    """
    send_read_PuTTY.send("Napište křestní jméno admina: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    krestni_jmeno = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    send_read_PuTTY.send("Napište příjmení admina: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    prijmeni = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    send_read_PuTTY.send("Napište přihlašovací jméno admina: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    prihlasovaci_jmeno = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    x = send_read_PuTTY.read(conn, addr)
    send_read_PuTTY.send("Napište heslo admina: ", conn, addr)
    heslo = send_read_PuTTY.read(conn, addr)
    try:
        admin_CRUD.create(connection, krestni_jmeno, prijmeni, prihlasovaci_jmeno, heslo)
        send_read_PuTTY.send("Admin vytvořen", conn, addr)
        send_read_PuTTY.send("Done", conn, addr)
    except:
        send_read_PuTTY.send("Error: AC002",conn,addr)

def R_admin(connection,conn,addr):
    """
        Použivá admin CRUD Read
        :param connection: připojení databáze
        :param conn: připojení clienta
        :param addr: ip clienta
        :return:
        """
    try:
        x = admin_CRUD.read(connection)
        x = str(x)
        send_read_PuTTY.send(x,conn,addr)
        send_read_PuTTY.send("Done",conn,addr)
    except:
        send_read_PuTTY.send("Error: AR001",conn,addr)

def U_admin(connection,conn,addr):
    """
        Použivá admin CRUD Update
        :param connection: připojení databáze
        :param conn: připojení clienta
        :param addr: ip clienta
        :return:
        """
    send_read_PuTTY.send("Napište sloupec: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    sloupec = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    send_read_PuTTY.send("Napište id: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    id = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    send_read_PuTTY.send("Napište novou proměnnou: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    prom = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    try:
        admin_CRUD.update(connection,sloupec,id,prom)
        send_read_PuTTY.send("Done", conn, addr)
    except:
        send_read_PuTTY.send("Error: AU001",conn,addr)

def D_admin(connection,conn,addr):
    """
        Použivá admin CRUD Delete
        :param connection: připojení databáze
        :param conn: připojení clienta
        :param addr: ip clienta
        :return:
        """
    send_read_PuTTY.send("Napište id: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    id = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    try:
        admin_CRUD.delete(connection,id)
        send_read_PuTTY.send("Done", conn, addr)
    except:
        send_read_PuTTY.send("Error AD001",conn,addr)

def C_autor(connection,conn,addr):
    """
        Použivá autor CRUD Create
        :param connection: připojení databáze
        :param conn: připojení clienta
        :param addr: ip clienta
        :return:
        """
    send_read_PuTTY.send("Napište křestní jméno autora: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    jmeno = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    send_read_PuTTY.send("Napište příjmení autora: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    prijmeni = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    send_read_PuTTY.send("Napište email autora: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    email = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    send_read_PuTTY.send("Napište přihlašovací jméno autora: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    prihlasovaci_jmeno = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    x = send_read_PuTTY.read(conn, addr)
    send_read_PuTTY.send("Napište heslo autora: ", conn, addr)
    heslo = send_read_PuTTY.read(conn, addr)
    try:
        autor_CRUD.create(connection,jmeno,prijmeni,email,prihlasovaci_jmeno,heslo,"1")
        send_read_PuTTY.send("Autor vytvořen", conn, addr)
        send_read_PuTTY.send("Done", conn, addr)
    except:
        send_read_PuTTY.send("Error: AC003",conn,addr)

def R_autor(connection,conn,addr):
    """
        Použivá autor CRUD Read
        :param connection: připojení databáze
        :param conn: připojení clienta
        :param addr: ip clienta
        :return:
        """
    try:
        x = autor_CRUD.read(connection)
        x = str(x)
        send_read_PuTTY.send(x,conn,addr)
        send_read_PuTTY.send("Done",conn,addr)
    except:
        send_read_PuTTY.send("Error: AR002",conn,addr)

def U_autor(connection,conn,addr):
    """
    Použivá autor CRUD Update
    :param connection: připojení databáze
    :param conn: připojení clienta
    :param addr: ip clienta
    :return:
    """
    send_read_PuTTY.send("Napište sloupec: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    sloupec = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    send_read_PuTTY.send("Napište id: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    id = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    send_read_PuTTY.send("Napište novou proměnnou: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    prom = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    try:
        autor_CRUD.update(connection,sloupec,id,prom)
        send_read_PuTTY.send("Done", conn, addr)
    except:
        send_read_PuTTY.send("Error: AU002",conn,addr)

def D_autor(connection,conn,addr):
    """
    Použivá autor CRUD Delete
    :param connection: připojení databáze
    :param conn: připojení clienta
    :param addr: ip clienta
    :return:
    """
    send_read_PuTTY.send("Napište id: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    id = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    try:
        autor_CRUD.delete(connection,id)
        send_read_PuTTY.send("Done", conn, addr)
    except:
        send_read_PuTTY.send("Error AD002",conn,addr)

def C_ban(connection,conn,addr):
    """
    Použivá ban CRUD Create
    :param connection: připojení databáze
    :param conn: připojení clienta
    :param addr: ip clienta
    :return:
    """
    send_read_PuTTY.send("Napište nové zabanované slovo: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    slovo = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    try:
        zabanovana_slova_CRUD.create(connection,slovo)
        send_read_PuTTY.send("Zabanovane slovo vytvořeno", conn, addr)
        send_read_PuTTY.send("Done", conn, addr)
    except:
        send_read_PuTTY.send("Error: AC003",conn,addr)

def R_ban(connection,conn,addr):
    """
        Použivá ban CRUD Read
        :param connection: připojení databáze
        :param conn: připojení clienta
        :param addr: ip clienta
        :return:
        """
    try:
        x = zabanovana_slova_CRUD.read(connection)
        x = str(x)
        send_read_PuTTY.send(x,conn,addr)
        send_read_PuTTY.send("Done",conn,addr)
    except:
        send_read_PuTTY.send("Error: AR003",conn,addr)

def U_ban(connection,conn,addr):
    """
        Použivá ban CRUD Update
        :param connection: připojení databáze
        :param conn: připojení clienta
        :param addr: ip clienta
        :return:
        """
    send_read_PuTTY.send("Napište sloupec: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    sloupec = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    send_read_PuTTY.send("Napište id: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    id = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    send_read_PuTTY.send("Napište novou proměnnou: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    prom = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    try:
        zabanovana_slova_CRUD.update(connection,sloupec,id,prom)
        send_read_PuTTY.send("Done", conn, addr)
    except:
        send_read_PuTTY.send("Error: AU003",conn,addr)

def D_ban(connection,conn,addr):
    """
        Použivá ban CRUD Delete
        :param connection: připojení databáze
        :param conn: připojení clienta
        :param addr: ip clienta
        :return:
        """
    send_read_PuTTY.send("Napište id: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    id = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    try:
        zabanovana_slova_CRUD.delete(connection,id)
        send_read_PuTTY.send("Done", conn, addr)
    except:
        send_read_PuTTY.send("Error AD003",conn,addr)