import tkinter as tk
from tkinter import PhotoImage
import registration
from methods import client_metody
import error
import app
import configurace

def prihlaseni(s):
    """
    Otevře login okno
    :param s: objekt připojí klienta
    :return:
    """
    root = tk.Tk()
    root.title("Přihlášení")
    root.geometry("550x600")
    root.resizable(False, False)

    formular = tk.Frame(root)
    formular.pack(fill=tk.BOTH, padx=10, pady=10)

    image = PhotoImage(file="omega.png")
    label = tk.Label(formular, image=image)
    label.image = image
    label.pack(side=tk.TOP, fill=tk.BOTH)


    text = tk.Label(formular, text="Přihlašovací jméno:", font=("Arial", 14))
    text.pack(padx=5, pady=5)

    jmeno = tk.Entry(formular, font=("Arial", 14))
    jmeno.pack(padx=5, pady=5)

    text = tk.Label(formular, text="Heslo:", font=("Arial", 14))
    text.pack(padx=5, pady=5)

    heslo = tk.Entry(formular, font=("Arial", 14))
    heslo.pack(padx=5, pady=5)


    box = tk.Frame(formular)
    box.pack(padx=5, pady=5)

    tlacitko_odejit_l = tk.Button(box, text="Odejít", width=10, command=root.destroy)
    tlacitko_odejit_l.pack(side=tk.LEFT, padx=5, pady=5)

    tlacitko_reg_l = tk.Button(box, text="Zaregistrovat", width=10)
    tlacitko_reg_l.pack(side=tk.LEFT, padx=5, pady=5)

    tlacitko_log_l = tk.Button(box, text="Přihlásit", width=10)
    tlacitko_log_l.pack(side=tk.LEFT, padx=5, pady=5)

    tlacitko_konf_l = tk.Button(box, text="Konfigurovat", width=10)
    tlacitko_konf_l.pack(side=tk.LEFT, padx=5, pady=5)

    def reg():
        """
        Reaguje na zmáčknutí tlačítka Registrovat a otevře okno registrace
        :return:
        """
        root.destroy()
        registration.registrace(s)

    tlacitko_reg_l.configure(command=reg)

    def get_log():
        """
        Reaguje na zmáčknutí tlačítka Přihlásit, zkontroluje zda uživatel nemá ban a otevře aplikaci
        :return:
        """
        jm = jmeno.get()
        he = heslo.get()
        x = client_metody.login_com(s,jm,he)
        if x == "Y":
            root.destroy()
            app.aplik(s,jm)
        if x == "N":
            error.err("Neplatné přihlašovací údaje")
        if x == "Ban":
            error.err("Na tomto serveru je tento uživatel zabanován.")

    tlacitko_log_l.configure(command=get_log)

    def config():
        """
        Reaguje na zmáčknutí tlačítka Konfigurace, otevře okno konigurace
        :return:
        """
        configurace.konf(s)

    tlacitko_konf_l.configure(command=config)

    root.mainloop()