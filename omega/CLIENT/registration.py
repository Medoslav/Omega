import tkinter as tk
from tkinter import PhotoImage
import login
from methods import client_metody
import error
import app
import configurace

def registrace(s):
    """
    Otevře registrační okno
    :param s: objekt připojí klienta
    :return:
    """
    root = tk.Tk()
    root.title("Registrace")
    root.geometry("550x800")
    root.resizable(False, False)

    formular = tk.Frame(root)
    formular.pack(fill=tk.BOTH, padx=10, pady=10)

    image = PhotoImage(file="omega.png")
    label = tk.Label(formular, image=image)
    label.image = image
    label.pack(side=tk.TOP, fill=tk.BOTH)

    text = tk.Label(formular, text="Křestní jméno:", font=("Arial", 14))
    text.pack(padx=5, pady=5)

    jmeno = tk.Entry(formular, font=("Arial", 14))
    jmeno.pack(padx=5, pady=5)

    text = tk.Label(formular, text="Příjmení:", font=("Arial", 14))
    text.pack(padx=5, pady=5)

    prijmeni = tk.Entry(formular, font=("Arial", 14))
    prijmeni.pack(padx=5, pady=5)

    text = tk.Label(formular, text="Email:", font=("Arial", 14))
    text.pack(padx=5, pady=5)

    email = tk.Entry(formular, font=("Arial", 14))
    email.pack(padx=5, pady=5)

    text = tk.Label(formular, text="Přihlašovací jméno:", font=("Arial", 14))
    text.pack(padx=5, pady=5)

    prezdivka = tk.Entry(formular, font=("Arial", 14))
    prezdivka.pack(padx=5, pady=5)

    text = tk.Label(formular, text="Heslo:", font=("Arial", 14))
    text.pack(padx=5, pady=5)

    heslo = tk.Entry(formular, font=("Arial", 14))
    heslo.pack(padx=5, pady=5)

    box = tk.Frame(formular)
    box.pack(padx=5, pady=5)

    tlacitko_odejit_r = tk.Button(box, text="Odejít", width=10, command=root.destroy)
    tlacitko_odejit_r.pack(side=tk.LEFT, padx=5, pady=5)

    tlacitko_log_r = tk.Button(box, text="Přihlásit", width=10)
    tlacitko_log_r.pack(side=tk.LEFT, padx=5, pady=5)

    tlacitko_reg_r = tk.Button(box, text="Zaregistrovat", width=10)
    tlacitko_reg_r.pack(side=tk.LEFT, padx=5, pady=5)

    tlacitko_konf_l = tk.Button(box, text="Konfigurovat", width=10)
    tlacitko_konf_l.pack(side=tk.LEFT, padx=5, pady=5)

    def log():
        """
        Reaguje na zmáčknutí tlačítka Přihlásit a otevře okno login
        :return:
        """
        root.destroy()
        login.prihlaseni()

    tlacitko_log_r.configure(command=log)

    def get_reg():
        """
        Reaguje na zmáčknutí tlačítka Registrovat, zkontroluje zda uživatel nemá ban a otevře aplikaci a odešle registrčku na server
        :return:
        """
        jm = jmeno.get()
        pr = prijmeni.get()
        em = email.get()
        pre = prezdivka.get()
        he = heslo.get()
        client_metody.mg(jm,pr,em,pre,he)
        x = client_metody.reg_com(s,jm,pr,em,pre,he)
        if x == "Y":
            root.destroy()
            app.aplik(s,pre)
        elif x == "N1":
            error.err("Uživatel již existuje změň jméno nebo email.")
        elif x == "N2":
            error.err("Neplatný email.")


    tlacitko_reg_r.configure(command=get_reg)

    def config():
        """
        Reaguje na zmáčknutí tlačítka Konfigurace, otevře okno konigurace
        :return:
        """
        configurace.konf(s)

    tlacitko_konf_l.configure(command=config)

    root.mainloop()