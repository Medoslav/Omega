from PuTTY_server import server
from DB_client import pripojeni_db
import server_load
import DB_load

x = server_load.nacti_ip_address()
ip = str(x)
x = server_load.nacti_port()
port = int(x)

x = DB_load.nacti_host()
host = str(x)
x = DB_load.nacti_user()
user = str(x)
x = DB_load.nacti_heslo()
password = str(x)

connection = pripojeni_db.start_DB(host,user,password)

server.start_server(ip,port,connection)