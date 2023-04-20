from SERVER.DB_client.CRUD import admin_CRUD
from SERVER.PuTTY_server import send_read_PuTTY
from SERVER.DB_client.DB_methods import DB_admin_metody
from SERVER.admin import admin_commands1
from SERVER.admin import admin_commands2
import time

def run(conn,addr,connection):
    """
    Spustí admin loop, pokud ještě žádný admin není tak ho vytvoří, přijímá příkazy z PuTTy
    :param conn: připojení clienta
    :param addr: ip clienta
    :param connection: připojení databáze
    :return:
    """
    while True:
        x = admin_CRUD.read(connection)

        if len(x) == 0:
            send_read_PuTTY.send("Výtej při prvním spuštění serveru. Pro pokračování musíš založit nového admina.", conn,addr)
            time.sleep(0.5)
            send_read_PuTTY.send("Napište své křestní jméno: ", conn, addr)
            x = send_read_PuTTY.read(conn,addr)
            krestni_jmeno = send_read_PuTTY.read(conn, addr)
            time.sleep(0.5)
            send_read_PuTTY.send("Napište své příjmení: ", conn, addr)
            x = send_read_PuTTY.read(conn,addr)
            prijmeni = send_read_PuTTY.read(conn, addr)
            time.sleep(0.5)
            send_read_PuTTY.send("Napište své přihlašovací jméno: ", conn, addr)
            x = send_read_PuTTY.read(conn,addr)
            prihlasovaci_jmeno = send_read_PuTTY.read(conn, addr)
            time.sleep(0.5)
            x = send_read_PuTTY.read(conn,addr)
            send_read_PuTTY.send("Napište své heslo: ", conn, addr)
            heslo = send_read_PuTTY.read(conn, addr)
            try:
                admin_CRUD.create(connection, krestni_jmeno, prijmeni, prihlasovaci_jmeno, heslo)
                send_read_PuTTY.send("Admin vytvořen", conn, addr)
            except:
                send_read_PuTTY.send("Error: AC001")
        else:
            send_read_PuTTY.send("Přihlašovací jméno: ", conn, addr)
            x = send_read_PuTTY.read(conn, addr)
            prihlasovaci_jmeno = send_read_PuTTY.read(conn, addr)
            time.sleep(0.5)
            x = send_read_PuTTY.read(conn, addr)
            send_read_PuTTY.send("Heslo: ", conn, addr)
            heslo = send_read_PuTTY.read(conn, addr)

            hesloDB = DB_admin_metody.admin_login(connection,prihlasovaci_jmeno)

            if hesloDB == heslo:
                send_read_PuTTY.send("Přihlášeno ",conn,addr)
                prihlasen = 1
                while prihlasen == 1:
                    send_read_PuTTY.send("\n"+"#",conn,addr)
                    x = send_read_PuTTY.read(conn,addr)
                    print(x)
                    if x == "Cadmin":
                        admin_commands1.C_admin(connection,conn,addr)
                    elif x == "Radmin":
                        admin_commands1.R_admin(connection,conn,addr)
                    elif x == "Uadmin":
                        admin_commands1.U_admin(connection,conn,addr)
                    elif x == "Dadmin":
                        admin_commands1.D_admin(connection,conn,addr)
                    elif x == "Cautor":
                        admin_commands1.C_autor(connection,conn,addr)
                    elif x == "Rautor":
                        admin_commands1.R_autor(connection,conn,addr)
                    elif x == "Uautor":
                        admin_commands1.U_autor(connection,conn,addr)
                    elif x == "Dautor":
                        admin_commands1.D_autor(connection,conn,addr)
                    elif x == "Cban":
                        admin_commands1.C_ban(connection,conn,addr)
                    elif x == "Rban":
                        admin_commands1.R_ban(connection,conn,addr)
                    elif x == "Uban":
                        admin_commands1.U_ban(connection,conn,addr)
                    elif x == "Dban":
                        admin_commands1.R_ban(connection,conn,addr)
                    elif x == "Cclanek":
                        admin_commands2.C_clanek(connection,conn,addr)
                    elif x == "Rclanek":
                        admin_commands2.R_clanek(connection,conn,addr)
                    elif x == "Uclanek":
                        admin_commands2.U_clanek(connection,conn,addr)
                    elif x == "Dclanek":
                        admin_commands2.D_clanek(connection,conn,addr)
                    elif x == "Ckomenter":
                        admin_commands2.C_komentar(connection,conn,addr)
                    elif x == "Ukomentar":
                        admin_commands2.U_komenatr(connection,conn,addr)
                    elif x == "Dkomenatr":
                        admin_commands2.D_komentar(connection,conn,addr)
                    elif x == "Rkomentar":
                        admin_commands2.R_komentar(connection,conn,addr)
                    elif x == "Ipconf":
                        admin_commands2.ip_config(conn,addr)
                    elif x == "Banusername":
                        admin_commands2.user_ban_name(connection,conn,addr)
                    elif x == "Banemail":
                        admin_commands2.user_ban_email(connection,conn,addr)
                    elif x == "Unbanusername":
                        admin_commands2.user_unban_name(connection,conn,addr)
                    elif x == "Blacklist":
                        admin_commands2.blacklist(connection,conn,addr)
                    elif x == "Banslovo":
                        admin_commands2.user_slovo_ban(connection,conn,addr)
                    elif x == "Unbanslovo":
                        admin_commands2.user_slovo_unban(connection,conn,addr)
                    elif x == "Slovolist":
                        admin_commands2.blacklist_slovo(connection,conn,addr)
                    elif x == "":
                        pass


            else:
                send_read_PuTTY.send("Neplatné přihlašovací údaje "+"\n", conn, addr)
                print("Error: AL001")