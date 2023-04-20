def create(connection, autor_id:str, clanek_id:str, text:str, datum:str):
    """
    Create metoda na tabulku komentar
    :param connection: připojení databáze
    :param autor_id: id autora
    :param clanek_id: id clanku
    :param text: text clanku
    :param datum: datum
    :return:
    """
    cursor = connection.cursor()
    command = "INSERT INTO `omega`.`komentar` (`autor_id`, `clanek_id`, `text_komenatre`, `datum_komentare`) VALUES ('"+autor_id+"', '"+clanek_id+"', '"+text+"', '"+datum+"');"
    cursor.execute(command)
    connection.commit()

    print("Insert do komentar: autor_id: "+autor_id+" text: "+text+" datum: "+datum)

def read(connection):
    """
    Create metoda na tabulku komentar
    :param connection: připojení databáze
    :return:
    """
    cursor = connection.cursor()
    command = "SELECT * FROM komentar;"
    cursor.execute(command)

    data = []
    for x in cursor:
        data.append(x)

    print("Read na komentar")

    return data

def update(connection,sloupec:str,id:str,nova_promena:str):
    """
    Update metoda na tabulku komenatr
    :param connection: připojení databáze
    :param sloupec: slopec v tabulce
    :param id: id
    :param nova_promena: nová proměnná
    :return:
    """
    cursor = connection.cursor()
    command = "UPDATE komentar SET "+sloupec+" = '"+nova_promena+"' WHERE id = '"+id+"'"
    cursor.execute(command)
    connection.commit()

    print("Update do komentar: sloupec: "+sloupec+" id: "+id+" nova_promena: "+nova_promena)

def delete(connection,id):
    """
    Delete metoda na tabulku komentar
    :param connection: připojení databáze
    :param id: id
    :return:
    """
    cursor = connection.cursor()
    command = "DELETE FROM komentar WHERE id = " + id + ";"
    cursor.execute(command)
    connection.commit()

    print("Delete v komentar: id: "+id)