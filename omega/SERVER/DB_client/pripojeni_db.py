import mysql.connector
connection = None

def start_DB(host,user,password):
  """
  Připojení k databázi
  :param host: host
  :param user: username
  :param password: heslo
  :return: připojení databáze
  """

  connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password
  )
  cursor = connection.cursor()
  command = "use omega;"
  cursor.execute(command)

  print("Pripojeno.")
  return connection


