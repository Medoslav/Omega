import time

from SERVER.PuTTY_server import send_read_PuTTY
from SERVER.DB_client.DB_methods import DB_user_metody
import re
from SERVER.DB_client.CRUD import autor_CRUD

def log(conn,addr,connection):
    """
    Metoda pro přihlášení klienta
    :param conn: klinstké připojiní
    :param addr: klientská adresa
    :param connection: připojení databáze
    :return:
    """
    send_read_PuTTY.send("Y", conn, addr)
    jmeno = send_read_PuTTY.read(conn,addr)
    heslo = send_read_PuTTY.read(conn,addr)

    x = DB_user_metody.client_login(connection,jmeno)
    y = DB_user_metody.client_ban_check(connection,jmeno)
    y = str(y)

    if y == "1":
        return "Ban"

    if x == heslo:
        return "Y"
    else:
        return "N"

def reg(conn,addr,connection):
    """
    Metoda pro registraci klienta
    :param conn: klinstké připojiní
    :param addr: klientská adresa
    :param connection: připojení databáze
    :return:
    """
    send_read_PuTTY.send("Y",conn,addr)
    jmeno = send_read_PuTTY.read(conn,addr)
    prijmeni = send_read_PuTTY.read(conn,addr)
    email = send_read_PuTTY.read(conn,addr)
    prezdivka = send_read_PuTTY.read(conn,addr)
    heslo = send_read_PuTTY.read(conn,addr)

    x = DB_user_metody.client_reg_jm(connection,jmeno)

    if x == "N1":
        return "N1"

    x = DB_user_metody.client_reg_em(connection,email)

    if x == "N1":
        return "N1"

    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        autor_CRUD.create(connection,jmeno,prijmeni,email,prezdivka,heslo,"0")
        return "Y"
    else:
        return "N2"

def gcl(conn,addr,connection):
    """
    Metoda pro vytažení článku z databáze a odlesmání na klineta
    :param conn: klinstké připojiní
    :param addr: klientská adresa
    :param connection: připojení databáze
    :return:
    """
    send_read_PuTTY.send("Y", conn, addr)
    id = DB_user_metody.client_clan_id(connection)
    autor = DB_user_metody.client_aut_pr(connection,id)
    datum = DB_user_metody.client_clan_dat(connection,id)
    datum = str(datum)
    text = DB_user_metody.client_clan_text(connection,id)

    text = DB_user_metody.clanek_ban_check(connection,text)

    send_read_PuTTY.send(autor,conn,addr)
    time.sleep(0.1)
    send_read_PuTTY.send(datum,conn,addr)
    time.sleep(0.1)
    send_read_PuTTY.send(text,conn,addr)
    time.sleep(0.1)
    send_read_PuTTY.send(id,conn,addr)

def gco(conn,addr,connection):
    """
    Metoda pro vytažení komentáře z databáze a odlesmání na klineta
    :param conn: klinstké připojiní
    :param addr: klientská adresa
    :param connection: připojení databáze
    :return:
    """
    send_read_PuTTY.send("Y",conn,addr)
    id_cl = send_read_PuTTY.read(conn,addr)
    id_co = DB_user_metody.client_komentar_id(connection,id_cl)
    if len(id_co) > 10:
        id_co_de = []
        x = 1
        while x <= 10:
            prvek = id_co.pop(len(id_co)-x)
            id_co_de.append(prvek)
            x += 1
    else:
        id_co_de = []
        id_co_de.extend(id_co)

    x = len(id_co_de)-1
    if x == -1:
        return "N"
    vy_text = ""
    while x >= 0:
        autor = DB_user_metody.client_komentar_pr(connection,id_co_de[x])
        datum = DB_user_metody.client_komentar_dat(connection,id_co_de[x])
        text = DB_user_metody.client_komentar_text(connection,id_co_de[x])
        text = DB_user_metody.komentar_ban_check(connection,text)
        datum = str(datum)
        vy_text = vy_text + autor + "  "+datum+"\n"+text+"\n"
        x -= 1
    return vy_text

def cla(conn,addr,connection):
    """
    Metoda pro vytvoření článku
    :param conn: klinstké připojiní
    :param addr: klientská adresa
    :param connection: připojení databáze
    :return:
    """
    send_read_PuTTY.send("Y", conn, addr)
    jmeno = send_read_PuTTY.read(conn,addr)
    text = send_read_PuTTY.read(conn,addr)
    x = DB_user_metody.client_clanek_duplik(connection,text)
    if x == "Y":
        id = DB_user_metody.client_clanek_userid(connection,jmeno)
        date = DB_user_metody.client_clanek_date()
        id = str(id)
        date = str(date)
        DB_user_metody.client_clanek_imp(connection,id,text,date)
        send_read_PuTTY.send("Y",conn,addr)
    elif x == "N":
        send_read_PuTTY.send("N",conn,addr)

def kom(conn,addr,connection):
    """
    Metoda pro vztvoření komentáře
    :param conn: klinstké připojiní
    :param addr: klientská adresa
    :param connection: připojení databáze
    :return:
    """
    send_read_PuTTY.send("Y", conn, addr)
    jmeno = send_read_PuTTY.read(conn,addr)
    cl_id = send_read_PuTTY.read(conn,addr)
    text = send_read_PuTTY.read(conn,addr)
    x = DB_user_metody.client_komentar_duplik(connection,cl_id,text)
    if x == "Y":
        id = DB_user_metody.client_clanek_userid(connection,jmeno)
        date = DB_user_metody.client_clanek_date()
        id = str(id)
        date = str(date)
        cl_id = str(cl_id)
        DB_user_metody.client_komentar_imp(connection,id,cl_id,text,date)
        send_read_PuTTY.send("Y",conn,addr)
    elif x == "N":
        send_read_PuTTY.send("N",conn,addr)







