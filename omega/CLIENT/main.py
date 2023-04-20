import connection
import login
import load_config
import error

ip = load_config.nacti_ip_address()
port = load_config.nacti_port()
ip = str(ip)
s = None
try:
    s = connection.connect_to_server(ip, port)
    connection.send_message(s,"user")
    login.prihlaseni(s)
except:
    error.err("Neplatná konfigurace, pro správnou funkci jí změňte.")
    login.prihlaseni(s)











