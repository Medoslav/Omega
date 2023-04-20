def create(connection, autor_id:str, text:str, datum:str):
    """
    Create metoda na tabulku clanek
    :param connection: připojení databáze
    :param autor_id: id autora
    :param text: text clanku
    :param datum: datum clanku
    :return:
    """
    cursor = connection.cursor()
    command = "INSERT INTO `omega`.`clanek` (`autor_id`, `text_clanku`, `datum_clanku`) VALUES ('"+autor_id+"', '"+text+"', '"+datum+"');"
    cursor.execute(command)
    connection.commit()

    print("Insert do clanek: autor_id: "+autor_id+" text: "+text+" datum: "+datum)

def read(connection):
    """
    Create metoda na tabulku clanek
    :param connection: připojení databáze
    :return:
    """
    cursor = connection.cursor()
    command = "SELECT * FROM clanek;"
    cursor.execute(command)

    data = []
    for x in cursor:
        data.append(x)

    print("Read na clanek")

    return data

def update(connection,sloupec:str,id:str,nova_promena:str):
    """
    Update metoda na tabulku clanek
    :param connection: připojení databáze
    :param sloupec: slopec v tabulce
    :param id: id
    :param nova_promena: nová proměnná
    :return:
    """
    cursor = connection.cursor()
    command = "UPDATE clanek SET "+sloupec+" = '"+nova_promena+"' WHERE id = '"+id+"'"
    cursor.execute(command)
    connection.commit()

    print("Update do clanek: sloupec: "+sloupec+" id: "+id+" nova_promena: "+nova_promena)

def delete(connection,id):
    """
    Delete metoda na tabulku admin
    :param connection: připojení databáze
    :param id: id
    :return:
    """
    cursor = connection.cursor()
    command = "DELETE FROM clanek WHERE id = " + id + ";"
    cursor.execute(command)
    connection.commit()

    print("Delete v clanek: id: "+id)