def create(connection, slovo:str):
    """
    Create metoda na tabulku zabanovany_slova
    :param connection: připojení databáze
    :param slovo: slovo
    :return:
    """
    cursor = connection.cursor()
    command = "INSERT INTO `omega`.`zabanovany_slova` (`slovo`) VALUES ('"+slovo+"');"
    cursor.execute(command)
    connection.commit()

    print("Insert do zabanovany_slova: "+slovo)

def read(connection):
    """
    Create metoda na tabulku zabanovany_slova
    :param connection: připojení databáze
    :return:
    """
    cursor = connection.cursor()
    command = "SELECT * FROM zabanovany_slova;"
    cursor.execute(command)

    data = []
    for x in cursor:
        data.append(x)

    print("Read na zabanovany_slova")

    return data

def update(connection,sloupec:str,id:str,nova_promena:str):
    """
    Update metoda na tabulku zabanovany_slova
    :param connection: připojení databáze
    :param sloupec: slopec v tabulce
    :param id: id
    :param nova_promena: nová proměnná
    :return:
    """
    cursor = connection.cursor()
    command = "UPDATE zabanovany_slova SET "+sloupec+" = '"+nova_promena+"' WHERE id = '"+id+"'"
    cursor.execute(command)
    connection.commit()

    print("Update do zabanovany_slova: sloupec: "+sloupec+" id: "+id+" nova_promena: "+nova_promena)

def delete(connection,id):
    """
    Delete metoda na tabulku zabanovany_slova
    :param connection: připojení databáze
    :param id: id
    :return:
    """
    cursor = connection.cursor()
    command = "DELETE FROM zabanovany_slova WHERE id = " + id + ";"
    cursor.execute(command)
    connection.commit()

    print("Delete v zabanovany_slova: id: "+id)