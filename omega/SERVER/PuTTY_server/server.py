import socket
import threading
from SERVER.run import run_program

def start_server(ip:str,port:int,connection):
    """
    Metoda spouští server a vlastně celý program.
    :return: nic
    """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ip, port))
        s.listen()

        print(f"Server start on {ip}:{port}")

        while True:
            conn, addr = s.accept()
            # Pro každého připojeného klienta spustíme nový thread
            thread = threading.Thread(target=handle_client, args=(conn, addr, connection))
            thread.start()
            print(f"Client connection accepted from {conn}:{addr}")

def handle_client(conn, addr , connection):
    """
    Metoda slouží jako client ui, nabo jako rozcestník po zadání příkazu.
    :param conn: port připojeného uživatele
    :param addr: ip pripojeného uživatele
    :return: nic nevrací
    """
    while True:
        run_program(conn,addr,connection)
