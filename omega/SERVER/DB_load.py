import json

def nacti_soubor():
    """
    Metoda načte konfigurační soubor.
    :return: vrací konfigurační soubor.
    """
    conf_text = ""
    try:
        conf = open("config_DB.conf", "r")
    except:
        print("Nelze nacist kanfiguraci soubor")
    else:
        for line in conf:
            conf_text += line
        conf.close()
        return conf_text

def nacti_host():
    """
    Metoda načte ip z konfiguračního souboru.
    :return: vrací ip z konfiguračního souboru.
    """
    try:
        data = json.loads(nacti_soubor())
        return data['host']
    except:
        print("Nelze nacist host z konfiguracniho souboru")

def nacti_user():
    """
    Metoda načte port z konfiguračního souboru.
    :return: vrací port z konfiguračního souboru.
    """
    try:
        data = json.loads(nacti_soubor())
        return data['user']
    except:
        print("Nelze nacist user z konfiguracniho souboru")

def nacti_heslo():
    """
    Metoda načte port z konfiguračního souboru.
    :return: vrací port z konfiguračního souboru.
    """
    try:
        data = json.loads(nacti_soubor())
        return data['password']
    except:
        print("Nelze nacist heslo z konfiguracniho souboru")