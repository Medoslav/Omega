import time
from CLIENT import connection
from CLIENT.methods.snk.snl_exe import had

def login_com(s,jmeno,heslo):
    """
    Přihlášovaní klienta, klient odešle své přihlašovací údaje.
    :param s: objekt připojení klienta
    :param jmeno: jmeno uživatele
    :param heslo: heslo uživatele
    :return: návrat ze serveru
    """
    connection.send_message(s,"LOG")
    x = connection.receive_message(s)
    if x == "Y":
        connection.send_message(s,jmeno)
        time.sleep(0.1)
        connection.send_message(s,heslo)
        x = connection.receive_message(s)
        return x

def reg_com(s,jmeno,prijmeni,email,prezdivka,heslo):
    """
    Registrace klienta, odešle registrační formulář na server
    :param s: objekt připojení klienta
    :param jmeno: jmeno uživatele
    :param prijmeni: příjmení uživatele
    :param email: email uživatele
    :param prezdivka: prezdivka uživatele
    :param heslo: heslo uživatele
    :return: návrat ze serveru
    """
    connection.send_message(s,"REG")
    x = connection.receive_message(s)
    if x == "Y":
        connection.send_message(s,jmeno)
        time.sleep(0.1)
        connection.send_message(s,prijmeni)
        time.sleep(0.1)
        connection.send_message(s,email)
        time.sleep(0.1)
        connection.send_message(s,prezdivka)
        time.sleep(0.1)
        connection.send_message(s,heslo)
        x = connection.receive_message(s)
        return x


def get_cla(s):
    """
    Oděšle požadavek na článek na server
    :param s: objekt připojení klienta
    :return: článek ze serveru
    """
    connection.send_message(s,"GCL")
    x = connection.receive_message(s)
    if x == "Y":
        autor = connection.receive_message(s)
        datum = connection.receive_message(s)
        text = connection.receive_message(s)
        id = connection.receive_message(s)

        sp_text = autor+"    "+datum+"\n"+text
        return sp_text,id

def get_com(s,id_pub):
    """
    Oděšle požadavek na komentář na server
    :param s: objekt připojení klienta
    :return: komentář ze serveru
    """
    connection.send_message(s,"GCO")
    x = connection.receive_message(s)
    if x == "Y":
        connection.send_message(s,id_pub)
        text = connection.receive_message(s)

        return text

def send_cla(s,jm,text):
    """
    Odešle na server nový článek napsaný uživatelem
    :param s: objekt připojení klienta
    :param jm: jméno uživatele
    :param text: text článku
    :return: odpověď ze serveru
    """
    connection.send_message(s,"CLA")
    x = connection.receive_message(s)
    if x == "Y":
        connection.send_message(s,jm)
        time.sleep(0.1)
        connection.send_message(s,text)
        x = connection.receive_message(s)
        return x

def send_kom(s,jm,cl_id,text):
    """
    Odešle na server nový komentář napsaný uživatelem
    :param s: objekt připojení klienta
    :param jm: jméno uživatele
    :param cl_id: id článku ke kterému se komentář váže
    :param text: text komentáře
    :return: odpověď ze serveru
    """
    connection.send_message(s,"KOM")
    x = connection.receive_message(s)
    if x == "Y":
        connection.send_message(s,jm)
        time.sleep(0.1)
        connection.send_message(s,cl_id)
        time.sleep(0.1)
        connection.send_message(s,text)
        x = connection.receive_message(s)
        return x

def mg(jm,pr,em,un,he):
    """
    Metoda spustí minihru když se uživatel snaží zaregistrovat jako S N A K E
    :param jm: jméno uživatele
    :param pr: příjmení uživatele
    :param em: email uživatele
    :param un: přezdívka uživatele
    :param he: heslo uživatele
    :return:
    """
    if jm=="S":
        if pr=="N":
            if em=="A":
                if un=="K":
                    if he=="E":
                        had.start_game()