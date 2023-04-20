import time
from SERVER.PuTTY_server import send_read_PuTTY
from SERVER.DB_client.CRUD import clanek_CRUD
from SERVER.DB_client.CRUD import komentar_CRUD
from SERVER import server_load
from SERVER.DB_client.DB_methods import DB_admin_metody

def C_clanek(connection,conn,addr):
    """
    Použivá clanek CRUD Create
    :param connection: připojení databáze
    :param conn: připojení clienta
    :param addr: ip clienta
    :return:
    """
    send_read_PuTTY.send("Napište id autora: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    id_adm = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    send_read_PuTTY.send("Napište text clanku: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    text = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    x = send_read_PuTTY.read(conn, addr)
    send_read_PuTTY.send("Napište datum napsani clanku: ", conn, addr)
    datum = send_read_PuTTY.read(conn, addr)
    try:
        clanek_CRUD.create(connection, id_adm, text, datum)
        send_read_PuTTY.send("Clanek vytvořen", conn, addr)
        send_read_PuTTY.send("Done", conn, addr)
    except:
        send_read_PuTTY.send("Error: AC002",conn,addr)

def R_clanek(connection,conn,addr):
    """
    Použivá clanek CRUD Read
    :param connection: připojení databáze
    :param conn: připojení clienta
    :param addr: ip clienta
    :return:
    """
    try:
        x = clanek_CRUD.read(connection)
        x = str(x)
        send_read_PuTTY.send(x,conn,addr)
        send_read_PuTTY.send("Done",conn,addr)
    except:
        send_read_PuTTY.send("Error: AR001",conn,addr)

def U_clanek(connection,conn,addr):
    """
    Použivá clanek CRUD Update
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
        clanek_CRUD.update(connection,sloupec,id,prom)
        send_read_PuTTY.send("Done", conn, addr)
    except:
        send_read_PuTTY.send("Error: AU001",conn,addr)

def D_clanek(connection,conn,addr):
    """
    Použivá clanek CRUD Delete
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
        clanek_CRUD.delete(connection,id)
        send_read_PuTTY.send("Done", conn, addr)
    except:
        send_read_PuTTY.send("Error AD001",conn,addr)

def C_komentar(connection,conn,addr):
    """
    Použivá komentar CRUD Create
    :param connection: připojení databáze
    :param conn: připojení clienta
    :param addr: ip clienta
    :return:
    """
    send_read_PuTTY.send("Napište id autora: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    id_adm = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    send_read_PuTTY.send("Napište id clanku: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    id_cla = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    send_read_PuTTY.send("Napište text komentare: ", conn, addr)
    x = send_read_PuTTY.read(conn, addr)
    text = send_read_PuTTY.read(conn, addr)
    time.sleep(0.5)
    x = send_read_PuTTY.read(conn, addr)
    send_read_PuTTY.send("Napište datum napsani komenatre: ", conn, addr)
    datum = send_read_PuTTY.read(conn, addr)
    try:
        komentar_CRUD.create(connection, id_adm,id_cla, text, datum)
        send_read_PuTTY.send("Komentar vytvořen", conn, addr)
        send_read_PuTTY.send("Done", conn, addr)
    except:
        send_read_PuTTY.send("Error: AC003",conn,addr)

def R_komentar(connection,conn,addr):
    """
    Použivá komentar CRUD Read
    :param connection: připojení databáze
    :param conn: připojení clienta
    :param addr: ip clienta
    :return:
    """
    try:
        x = komentar_CRUD.read(connection)
        x = str(x)
        send_read_PuTTY.send(x,conn,addr)
        send_read_PuTTY.send("Done",conn,addr)
    except:
        send_read_PuTTY.send("Error: AR001",conn,addr)

def U_komenatr(connection,conn,addr):
    """
    Použivá komentar CRUD Update
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
        komentar_CRUD.update(connection,sloupec,id,prom)
        send_read_PuTTY.send("Done", conn, addr)
    except:
        send_read_PuTTY.send("Error: AU001",conn,addr)

def D_komentar(connection,conn,addr):
    """
    Použivá komentar CRUD Delete
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
        komentar_CRUD.delete(connection,id)
        send_read_PuTTY.send("Done", conn, addr)
    except:
        send_read_PuTTY.send("Error AD001",conn,addr)

def ip_config(conn,addr):
    """
    Změnění ip configu
    :param conn: připojení clienta
    :param addr: ip clienta
    :return:
    """
    send_read_PuTTY.send("Napiš ip adresu:",conn,addr)
    x = send_read_PuTTY.read(conn, addr)
    id = send_read_PuTTY.read(conn, addr)
    send_read_PuTTY.send("Napiš ip port:",conn,addr)
    x = send_read_PuTTY.read(conn, addr)
    port = send_read_PuTTY.read(conn, addr)
    try:
        server_load.uprav_konfiguraci(id,port)
        send_read_PuTTY.send("Done", conn, addr)
    except:
        send_read_PuTTY.send("Error IP001", conn, addr)

def user_ban_name(connection,conn,addr):
    """
    Zabanování uživatele podle jména
    :param connection: připojení databáze
    :param conn: připojení clienta
    :param addr: ip clienta
    :return:
    """
    send_read_PuTTY.send("Napiš přihlašovací jméno uživatele kterého chceš zabanovat:",conn,addr)
    x = send_read_PuTTY.read(conn, addr)
    jmeno = send_read_PuTTY.read(conn,addr)
    print(jmeno)
    try:
        DB_admin_metody.ban_user_name(connection,jmeno)
    except:
        send_read_PuTTY.send("Error UB001", conn, addr)

def user_ban_email(connection,conn,addr):
    """
    Zabanování uživatele podle jména
    :param connection: připojení databáze
    :param conn: připojení clienta
    :param addr: ip clienta
    :return:
    """
    send_read_PuTTY.send("Napiš email uživatele kterého chceš zabanovat:",conn,addr)
    x = send_read_PuTTY.read(conn, addr)
    jmeno = send_read_PuTTY.read(conn,addr)
    try:
        DB_admin_metody.ban_email(connection,jmeno)
    except:
        send_read_PuTTY.send("Error UB001", conn, addr)

def user_unban_name(connection,conn,addr):
    """
    Odbanování uživatele podle jména
    :param connection: připojení databáze
    :param conn: připojení clienta
    :param addr: ip clienta
    :return:
    """
    send_read_PuTTY.send("Napiš přihlašovací jméno uživatele kterého chceš odbanovat:",conn,addr)
    x = send_read_PuTTY.read(conn, addr)
    jmeno = send_read_PuTTY.read(conn,addr)
    try:
        DB_admin_metody.ban_user_name(connection,jmeno)
        send_read_PuTTY.send("Done",conn,addr)
    except:
        send_read_PuTTY.send("Error UU001", conn, addr)

def blacklist(connection,conn,addr):
    """
    Vypsání zabanovaných uživatlů
    :param connection: připojení databáze
    :param conn: připojení clienta
    :param addr: ip clienta
    :return:
    """
    send_read_PuTTY.send("Zabanovaní uživatelé:"+"\n",conn,addr)
    x = DB_admin_metody.blacklist(connection)
    send_read_PuTTY.send(x,conn,addr)

def user_slovo_ban(connection,conn,addr):
    """
    Zabanování nového slova
    :param connection: připojení databáze
    :param conn: připojení clienta
    :param addr: ip clienta
    :return:
    """
    send_read_PuTTY.send("Napiš slovo který chceš zabanovat:",conn,addr)
    x = send_read_PuTTY.read(conn, addr)
    slovo = send_read_PuTTY.read(conn,addr)
    try:
        DB_admin_metody.ban_slovo(connection,slovo)
    except:
        send_read_PuTTY.send("Error UB001", conn, addr)

def user_slovo_unban(connection,conn,addr):
    """
    Odbanování nového slova
    :param connection: připojení databáze
    :param conn: připojení clienta
    :param addr: ip clienta
    :return:
    """
    send_read_PuTTY.send("Napiš slovo který chceš odbanovat:",conn,addr)
    x = send_read_PuTTY.read(conn, addr)
    jmeno = send_read_PuTTY.read(conn,addr)
    try:
        DB_admin_metody.ban_user_name(connection,jmeno)
        send_read_PuTTY.send("Done",conn,addr)
    except:
        send_read_PuTTY.send("Error UU001", conn, addr)

def blacklist_slovo(connection,conn,addr):
    """
    Vypsání zabanovaných slov
    :param connection: připojení databáze
    :param conn: připojení clienta
    :param addr: ip clienta
    :return:
    """
    send_read_PuTTY.send("Zabanovaná slova:"+"\n",conn,addr)
    x = DB_admin_metody.blacklist(connection)
    send_read_PuTTY.send(x,conn,addr)

