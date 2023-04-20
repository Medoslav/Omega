def create(connection,jmeno_admin:str, prijmeni_admin:str, prezdivka_admin:str, heslo_admin:str):
    """
    Create metoda na tabulku admin
    :param connection: připojení databáze
    :param jmeno_admin: jméno admina
    :param prijmeni_admin: příjmení admina
    :param prezdivka_admin: přezdívka admina
    :param heslo_admin: heslo admina
    :return:
    """
    cursor = connection.cursor()
    command = "INSERT INTO `omega`.`admin1` (`jmeno_admin`, `prijmeni_admin`, `prezdivka_admin`, `heslo_admin`) VALUES ('"+jmeno_admin+"', '"+prijmeni_admin+"', '"+prezdivka_admin+"', '"+heslo_admin+"');"
    cursor.execute(command)
    connection.commit()

    print("Insert do admin1: jmeno_admin: "+jmeno_admin+" prijmeni_admin: "+prijmeni_admin+" prezdivka_admin: "+prezdivka_admin+" heslo_admin: "+heslo_admin)

def read(connection):
    """
    Create metoda na tabulku admin
    :param connection: připojení databáze
    :return:
    """
    cursor = connection.cursor()
    command = "SELECT * FROM admin1;"
    cursor.execute(command)

    data = []
    for x in cursor:
        data.append(x)

    print("Read na admin1")

    return data

def update(connection,sloupec:str,id:str,nova_promena:str):
    """
    Update metoda na tabulku admin
    :param connection: připojení databáze
    :param sloupec: slopec v tabulce
    :param id: id
    :param nova_promena: nová proměnná
    :return:
    """
    cursor = connection.cursor()
    command = "UPDATE admin1 SET "+sloupec+" = '"+nova_promena+"' WHERE id = '"+id+"'"
    cursor.execute(command)
    connection.commit()

    print("Update do admin1: sloupec: "+sloupec+" id: "+id+" nova_promena: "+nova_promena)

def delete(connection,id):
    """
    Delete metoda na tabulku admin
    :param connection: připojení databáze
    :param id: id
    :return:
    """
    cursor = connection.cursor()
    command = "DELETE FROM admin1 WHERE id = " + id + ";"
    cursor.execute(command)
    connection.commit()

    print("Delete v admin1: id: "+id)