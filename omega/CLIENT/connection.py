import socket

def connect_to_server(ip: str, port: int):
    """
    Připojí se k serveru na zadané IP adrese a portu.
    :param ip: IP adresa serveru
    :param port: port serveru
    :return: objekt socket reprezentující klientovu připojení
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    return s

def send_message(s: socket.socket, message: str):
    """
    Odešle zprávu na server přes zadané socket připojení.
    :param s: objekt socket reprezentující klientovu připojení
    :param message: zpráva k odeslání na server
    :return: nic
    """
    s.sendall(message.encode())

def receive_message(s: socket.socket) -> str:
    """
    Přijme zprávu ze serveru přes zadané socket připojení.
    :param s: objekt socket reprezentující klientovu připojení
    :return: zpráva přijatá ze serveru
    """
    return s.recv(1024).decode()