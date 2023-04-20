import json

def nacti_soubor():
    """
    Metoda načte konfigurační soubor.
    :return: vrací konfigurační soubor.
    """
    conf_text = ""
    try:
        conf = open("config_server.conf", "r")
    except:
        print("Nelze nacist kanfiguraci soubor")
    else:
        for line in conf:
            conf_text += line
        conf.close()
        return conf_text

def nacti_ip_address():
    """
    Metoda načte ip z konfiguračního souboru.
    :return: vrací ip z konfiguračního souboru.
    """
    try:
        data = json.loads(nacti_soubor())
        return data['ip_address']
    except:
        print("Nelze nacist ip_address z konfiguracniho souboru")

def nacti_port():
    """
    Metoda načte port z konfiguračního souboru.
    :return: vrací port z konfiguračního souboru.
    """
    try:
        data = json.loads(nacti_soubor())
        return data['port']
    except:
        print("Nelze nacist port z konfiguracniho souboru")

def uprav_konfiguraci(ip, port):
    """
    Metoda upraví konfigurační soubor a uloží do něj nové hodnoty ip a port.
    :param ip: nová ip adresa.
    :param port: nový port.
    """
    try:
        data = json.loads(nacti_soubor())
        data['ip_address'] = ip
        data['port'] = port
        with open('config_server.conf', 'w') as outfile:
            json.dump(data, outfile)
    except:
        print("Nelze upravit konfiguracni soubor")

