def create(connection, jmeno_autor:str, prijmeni_autor:str, email_autor:str, prezdivka_autor:str, heslo_autor:str, ban:str):
    """
    Create metoda na tabulku autor
    :param connection: připojení databáze
    :param jmeno_autor: jméno autor
    :param prijmeni_autor: příjmení autor
    :param email_autor: email autor
    :param prezdivka_autor: přezdívka autor
    :param heslo_autor: heslo autor
    :param ban: ban autor
    :return:
    """
    cursor = connection.cursor()
    command = "INSERT INTO `omega`.`autor` (`jmeno_autor`, `prijmeni_autor`, `email_autor`, `prezdivka_autor`, `heslo_autor`, `ban`) VALUES ('"+jmeno_autor+"', '"+prijmeni_autor+"', '"+email_autor+"', '"+prezdivka_autor+"', '"+heslo_autor+"', '"+ban+"');"
    cursor.execute(command)
    connection.commit()

    print("Insert do autor: jmeno: "+jmeno_autor+" prijmeni: "+prijmeni_autor+" email: "+email_autor+" prezdivka: "+prezdivka_autor+" heslo: "+heslo_autor+" ban: "+ban)

def read(connection):
    """
    Create metoda na tabulku autor
    :param connection: připojení databáze
    :return:
    """
    cursor = connection.cursor()
    command = "SELECT * FROM autor;"
    cursor.execute(command)

    data = []
    for x in cursor:
        data.append(x)

    print("Read na autor")

    return data

def update(connection,sloupec:str,id:str,nova_promena:str):
    """
    Update metoda na tabulku autor
    :param connection: připojení databáze
    :param sloupec: slopec v tabulce
    :param id: id
    :param nova_promena: nová proměnná
    :return:
    """
    cursor = connection.cursor()
    command = "UPDATE autor SET "+sloupec+" = '"+nova_promena+"' WHERE id = '"+id+"'"
    cursor.execute(command)
    connection.commit()

    print("Update do autor: sloupec: "+sloupec+" id: "+id+" nova_promena: "+nova_promena)

def delete(connection,id):
    """
    Delete metoda na tabulku autor
    :param connection: připojení databáze
    :param id: id
    :return:
    """
    cursor = connection.cursor()
    command = "DELETE FROM autor WHERE id = " + id + ";"
    cursor.execute(command)
    connection.commit()

    print("Delete v autor: id: "+id)