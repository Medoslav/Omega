import re

def injection(zprava):
    """
    Kontroluje jestli ve stringu není sql injection
    :param zprava: string
    :return: pokud je tak Y pokud není tak N
    """
    zakazane_znaky = re.compile(r'[-;\'"()&]')
    if zakazane_znaky.search(zprava):
        return "Y"
    else:
        return "N"
