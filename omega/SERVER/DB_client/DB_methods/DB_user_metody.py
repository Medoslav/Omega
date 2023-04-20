import random
from SERVER.DB_client.CRUD import clanek_CRUD
from SERVER.DB_client.CRUD import komentar_CRUD
from datetime import date

def client_login(connection,username):
    """
    Vezme jméno az kontroluje jestli je v databázi
    :param connection: připojení databáze
    :param username: přihlašovací jméno
    :return: Přihlašovací jméno nebo nic
    """
    cursor = connection.cursor()
    command = "SELECT heslo_autor FROM autor WHERE prezdivka_autor = '"+username+"';"
    try:
        cursor.execute(command)
        for x in cursor:
            heslo = x
        return heslo[0]
    except:
        return " "

def client_reg_jm(connection,username):
    """
    Vezme jméno az kontroluje jestli je v databázi
    :param connection: připojení databáze
    :param username: přihlašovací jméno
    :return:pokud přezdívka je v databázi tak vrátí N1 a pokud není tak vrátí Y
    """
    cursor = connection.cursor()
    jmeno = None
    command = "SELECT prezdivka_autor FROM autor WHERE prezdivka_autor = '" + username + "';"
    cursor.execute(command)
    for x in cursor:
        jmeno = x
    if jmeno != None:
        return "N1"
    else:
        return "Y"

def client_reg_em(connection,email):
    """
    Vezme email az kontroluje jestli je v databázi
    :param connection: připojení databáze
    :param email: přihlašovací jméno
    :return:pokud přezdívka je v databázi tak vrátí N1 a pokud není tak vrátí Y
        """
    cursor = connection.cursor()
    jmeno = None
    command = "SELECT email_autor FROM autor WHERE email_autor = '" + email + "';"
    cursor.execute(command)
    for x in cursor:
        jmeno = x
    if jmeno != None:
        return "N1"
    else:
        return "Y"

def client_clan_id(connection):
    """
    vrací háhodné id článku
    :param connection: připojení databáze
    :return: náhodné id
    """
    id = []
    cursor = connection.cursor()
    command = "SELECT id FROM clanek;"
    cursor.execute(command)
    for x in cursor:
        id.append(x[0])
    delka = len(id)-1
    nahodne_cislo = random.randint(0,delka)
    nahodne_id = id[nahodne_cislo]
    return str(nahodne_id)

def client_aut_pr(connection,id):
    """
    vezme id článku a vrátí přezdívku autora co ho napsal
    :param connection: připojení databáze
    :param id: id clanku
    :return: prezdivka autora
    """
    cursor = connection.cursor()
    command = "SELECT autor_id FROM clanek WHERE id = '"+id+"';"
    cursor.execute(command)
    for x in cursor:
        list = x
    autor_id = list[0]
    autor_id = str(autor_id)
    command = "SELECT prezdivka_autor FROM autor WHERE id = '"+autor_id+"';"
    cursor.execute(command)
    for x in cursor:
        list = x
    autor_pr = list[0]
    return autor_pr

def client_clan_dat(connection,id):
    """
    Vrátí datum článku
    :param connection: připojení
    :param id: id článku
    :return: datum napsání článku
    """
    cursor = connection.cursor()
    command = "SELECT datum_clanku FROM clanek WHERE id = '" + id + "';"
    cursor.execute(command)
    for x in cursor:
        list = x
    datum = list[0]
    return datum

def client_clan_text(connection,id):
    """
    Vrátí text článku
    :param connection: připojení databáze
    :param id: id článku
    :return: text clanku
    """
    cursor = connection.cursor()
    command = "SELECT text_clanku FROM clanek WHERE id = '" + id + "';"
    cursor.execute(command)
    for x in cursor:
        list = x
    text = list[0]
    return text

def client_komentar_id(connection,id_cl):
    """
    Vrátí id všech komentářů u komentáře
    :param connection: připojení databáze
    :param id_cl: id článku
    :return: id komentáře
    """
    list = []
    cursor = connection.cursor()
    command = "SELECT id FROM komentar WHERE clanek_id = '" + id_cl + "';"
    cursor.execute(command)
    for x in cursor:
        list.append(x[0])

    return list

def client_komentar_pr(connection,id_co):
    """
    Vrátí id atoura co napsal komentář
    :param connection: připojení databáze
    :param id_co: id comentáře
    :return: id autora
    """
    id_co = str(id_co)
    cursor = connection.cursor()
    command = "SELECT autor_id FROM komentar WHERE id = '" + id_co + "';"
    cursor.execute(command)
    for x in cursor:
        list = x
    autor_id = list[0]
    autor_id = str(autor_id)
    command = "SELECT prezdivka_autor FROM autor WHERE id = '" + autor_id + "';"
    cursor.execute(command)
    for x in cursor:
        list = x
    autor_pr = list[0]
    return autor_pr

def client_komentar_dat(connection,id_co):
    """
    Vráti datum komentáře
    :param connection: připojení databáze
    :param id_co: id komentáře
    :return: datum komentáře
    """
    id_co = str(id_co)
    cursor = connection.cursor()
    command = "SELECT datum_komentare FROM komentar WHERE id = '" + id_co + "';"
    cursor.execute(command)
    for x in cursor:
        list = x
    datum = list[0]
    return datum

def client_komentar_text(connection,id_co):
    """
    Vrátí text komentáře
    :param connection: připojení databáze
    :param id_co: id komentáře
    :return: text komentáře
    """
    id_co = str(id_co)
    cursor = connection.cursor()
    command = "SELECT text_komenatre FROM komentar WHERE id = '" + id_co + "';"
    cursor.execute(command)
    for x in cursor:
        list = x
    text = list[0]
    return text

def client_clanek_userid(connection,jmeno):
    """
    vypíše id autora podle přezdívky
    :param connection: připojení databáze
    :param jmeno: prezdivka autora
    :return: id autora
    """
    cursor = connection.cursor()
    command = "SELECT id FROM autor WHERE prezdivka_autor = '"+jmeno+"';"
    cursor.execute(command)
    for x in cursor:
        list = x
    text = list[0]
    return text

def client_clanek_date():
    """
    Vrátí dnešní datum
    :return: datum
    """
    dnes = date.today()
    datum = dnes.strftime("%Y-%m-%d")
    return datum

def client_clanek_imp(connection,id,text,date):
    clanek_CRUD.create(connection,id,text,date)

def client_clanek_duplik(connection,text):
    """
    Zkontroluje jestli je článek unikátní
    :param connection: připojení databáze
    :param text: text komentáře
    :return: pokud je komentář unikátní tak vrátí Y pokud ne tak N
    """
    cursor = connection.cursor()
    navrat = None
    command = "SELECT text_clanku FROM clanek WHERE text_clanku = '" + text + "';"
    cursor.execute(command)
    for x in cursor:
        navrat = x
    if navrat != None:
        return "N"
    else:
        return "Y"

def client_komentar_duplik(connection,cl_id,text):
    """
    Zkontroluje jestli je komentář unikátní
    :param connection: připojení databáze
    :param cl_id: id klienta
    :param text: text komentáře
    :return:
    """
    cursor = connection.cursor()
    navrat = None
    command = "SELECT text_komenatre FROM komentar WHERE text_komenatre = '" + text + "' AND clanek_id = '" + cl_id + "';"
    cursor.execute(command)
    for x in cursor:
        navrat = x
    if navrat != None:
        return "N"
    else:
        return "Y"

def client_komentar_imp(connection,au_id,cl_id,text,date):
    komentar_CRUD.create(connection,au_id,cl_id,text,date)

def client_ban_check(connection,jmeno):
    """
    kontroluje jestli uživatel nemá ban
    :param connection: připojení databáze
    :param jmeno: přezdívka uživatele
    :return: číslo jestli je zabanovanej
    """
    cursor = connection.cursor()
    command = "SELECT ban FROM autor WHERE prezdivka_autor = '" + jmeno + "';"
    cursor.execute(command)
    for x in cursor:
        ban = x
    return ban[0]

def clanek_ban_check(connection,text):
    """
    Kontroluje jestli ve článku nejsou zabanovaný slova a cenzuruje je
    :param connection: připojení databáze
    :param text: text článku
    :return: zkontrolovaný text článku
    """
    slova=[]
    cursor = connection.cursor()
    command = "SELECT slovo FROM zabanovany_slova;"
    cursor.execute(command)
    for x in cursor:
        slova.append(x[0])

    for word in slova:
        if word in text:
            replacement = '*' * len(word)
            text = text.replace(word, replacement)
    return text

def komentar_ban_check(connection,text):
    """
    Kontroluje jestli ve komentáři nejsou zabanovaný slova a cenzuruje je
    :param connection: připojení databáze
    :param text: text komentáře
    :return: zkontrolovaný text komentáře
    """
    slova=[]
    cursor = connection.cursor()
    command = "SELECT slovo FROM zabanovany_slova;"
    cursor.execute(command)
    for x in cursor:
        slova.append(x[0])

    for word in slova:
        if word in text:
            replacement = '*' * len(word)
            text = text.replace(word, replacement)
    return text