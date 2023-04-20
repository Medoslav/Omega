import tkinter as tk
import load_config
import error

def konf(s):
    """
    Otevře okno na konfiguraci připojení na server
    :param s: objekt připojí klienta
    :return:
    """
    root = tk.Tk()
    root.title("Configurace")
    root.geometry("300x250")
    root.resizable(False, False)

    formular = tk.Frame(root)
    formular.pack(fill=tk.BOTH, padx=10, pady=10)

    text = tk.Label(formular, text="IP adresa:", font=("Arial", 14))
    text.pack(padx=5, pady=5)

    ip = tk.Entry(formular, font=("Arial", 14))
    ip.pack(padx=5, pady=5)

    text = tk.Label(formular, text="Port:", font=("Arial", 14))
    text.pack(padx=5, pady=5)

    port = tk.Entry(formular, font=("Arial", 14))
    port.pack(padx=5, pady=5)


    box = tk.Frame(formular)
    box.pack(padx=5, pady=5)

    tlacitko_odejit_l = tk.Button(box, text="Zpět", width=10, command=root.destroy)
    tlacitko_odejit_l.pack(side=tk.LEFT, padx=5, pady=5)

    tlacitko_konf_l = tk.Button(box, text="Uložit", width=10)
    tlacitko_konf_l.pack(side=tk.LEFT, padx=5, pady=5)

    def get_log():
        """
        Reaguje na stisk tlačítka Uložit, uloží novou konfiguraci
        :return:
        """
        i = ip.get()
        p = port.get()
        i = str(i)
        p = int(p)
        load_config.uprav_konfiguraci(i,p)
        error.err("Konfigurace uložena, pro provedení změn restartujte aplikaci.")

    tlacitko_konf_l.configure(command=get_log)
