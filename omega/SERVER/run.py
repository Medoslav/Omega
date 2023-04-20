from PuTTY_server import send_read_PuTTY
from admin import admin_ui
from client import client_ui

def run_program(conn,addr,connection):
    x = send_read_PuTTY.read(conn,addr)

    if x == "admin":
        admin_ui.run(conn,addr,connection)

    if x == "user":
        client_ui.run(conn,addr,connection)


