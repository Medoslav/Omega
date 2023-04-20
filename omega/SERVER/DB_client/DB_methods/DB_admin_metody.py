def admin_login(connection,username):
    """
    Zajišťuje příhlášení admina
    :param connection: připojení databáze
    :param username: přihlašovací jméno
    :return:
    """
    cursor = connection.cursor()
    command = "SELECT heslo_admin FROM admin1 WHERE prezdivka_admin = '"+username+"';"
    try:
        cursor.execute(command)
        for x in cursor:
            heslo = x
        return heslo[0]
    except:
        return " "

def ban_user_name(connection,username):
    """
    Zabanování uživatele podle jména
    :param connection: připojení databáze
    :param username: jméno aživatele
    :return:
    """
    cursor = connection.cursor()
    command = "UPDATE autor SET ban = '1' WHERE prezdivka_autor = '"+username+"'"
    cursor.execute(command)
    connection.commit()

def ban_email(connection,email):
    """
    Zabanování uživatele podle emailu
    :param connection: připojení databáze
    :param email: email uživatele
    :return:
    """
    cursor = connection.cursor()
    command = "UPDATE autor SET ban = '1' WHERE email_autor = '"+email+"'"
    cursor.execute(command)
    connection.commit()

def unban_user_name(connection,username):
    """
    Odbanování uživatele
    :param connection: připojení databáze
    :param username: jméno uživatele
    :return:
    """
    cursor = connection.cursor()
    command = "UPDATE autor SET ban = '0' WHERE prezdivka_autor = '"+username+"'"
    cursor.execute(command)
    connection.commit()

def blacklist(connection):
    """
    Vypsání všech zabanovaných uživatlů
    :param connection: připojení databáze
    :return:
    """
    bllist = []
    cursor = connection.cursor()
    command = "SELECT prezdivka_autor FROM autor WHERE ban = 1;"
    cursor.execute(command)
    for x in cursor:
        bllist.append(x[0])
    navrat = ', '.join(bllist)
    return navrat

def ban_slovo(connection,slovo):
    """
    Zabanovat nové slovo
    :param connection: připojení databáze
    :param slovo: slovo
    :return:
    """
    cursor = connection.cursor()
    command = "INSERT INTO `omega`.`zabanovany_slova` (`slovo`) VALUES ('"+slovo+"');"
    cursor.execute(command)
    connection.commit()

def unban_slovo(connection,slovo):
    """
    Odbanovat slovo
    :param connection: připojení databáze
    :param slovo: slovo
    :return:
    """
    cursor = connection.cursor()
    command = "DELETE FROM zabanovany_slova WHERE slovo = " + slovo + ";"
    cursor.execute(command)
    connection.commit()

def slova_ban(connection):
    """
    Vypsání všech zabanovaných slov
    :param connection: připojení databáze
    :return:
    """
    bllist = []
    cursor = connection.cursor()
    command = "SELECT slovo FROM zabanovany_slova;"
    cursor.execute(command)
    for x in cursor:
        bllist.append(x[0])
    navrat = ', '.join(bllist)
    return navrat