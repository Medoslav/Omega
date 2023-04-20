from SERVER.PuTTY_server import send_read_PuTTY
from SERVER.client import client_commands

def run(conn,addr,connection):
    """
    Spustí loop pro klientské ovládání a přijímání příkazů
    :param conn: klinstké připojiní
    :param addr: klientská adresa
    :param connection: připojení databáze
    :return:
    """
    while True:

        x = send_read_PuTTY.read(conn, addr)

        if x == "LOG":
            x = client_commands.log(conn,addr,connection)
            send_read_PuTTY.send(x,conn,addr)

        if x == "REG":
            x = client_commands.reg(conn,addr,connection)
            send_read_PuTTY.send(x,conn,addr)

        if x == "GCL":
            client_commands.gcl(conn,addr,connection)

        if x == "GCO":
            x = client_commands.gco(conn,addr,connection)
            send_read_PuTTY.send(x,conn,addr)

        if x == "CLA":
            client_commands.cla(conn,addr,connection)

        if x == "KOM":
            client_commands.kom(conn,addr,connection)
