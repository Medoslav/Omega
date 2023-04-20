from SERVER.PuTTY_server import SQL_injection

def send (zprava,conn, addr):
    """
    Metoda odešle zprávu zpátky uživateli.
    :param zprava: Správa pro odeslání.
    :param conn: Port uživatele kterému se má zpráva odeslat.
    :param addr: Ip uživatele kterému se má zpráva odeslat.
    :return: nic nevrací
    """
    message_as_bytes = bytes(zprava, "utf-8")
    conn.send(message_as_bytes)

def read (conn,addr):
    """
    Metoda přijme zprávu od uživatele.
    :param conn: Port uživatele kterému se má zpráva odeslat.
    :param addr: Ip uživatele kterému se má zpráva odeslat.
    :return: vrací příkaz co napsal uživatel do konzole.
    """
    message_as_bites = conn.recv(1024)
    zprava = message_as_bites.decode()
    x = SQL_injection.injection(zprava)
    if x == "Y":
        pass
    else:
        return zprava