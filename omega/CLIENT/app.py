import tkinter as tk
from tkinter import scrolledtext
from CLIENT.methods import client_metody
import clanek
import komentar

def aplik(s,jm):
    """
    Spuští samotnou okení aplikaci sociální sítě
    :param s: objekt připojí klienta
    :param jm: jméno klienta
    :return:
    """
    root = tk.Tk()
    root.geometry("850x650")
    root.title("Omega.exe")

    # Vytvoření rámečku pro zobrazování článku
    text_cl, id_cl = client_metody.get_cla(s)
    article_text_cl = text_cl
    article_frame = tk.Frame(root, bd=2, relief="sunken")
    article_display = scrolledtext.ScrolledText(article_frame, width=70, height=15, font=("Arial", 12))
    article_display.insert("end", article_text_cl)
    article_display.pack(expand=True, fill="both")
    article_frame.pack(side="top", padx=10, pady=10, expand=True, fill="both")

    # Vytvoření posuvníku pro zobrazování komentářů
    text_co = client_metody.get_com(s, id_cl)
    if text_co == "N":
        comments_frame = tk.Frame(root, bd=2, relief="sunken")
        comments_display = scrolledtext.ScrolledText(comments_frame, width=50, height=10, font=("Arial", 12))
        comments_display.pack(expand=True, fill="both")
        comments_frame.pack(side="left", padx=10, pady=10, expand=True, fill="both")
    else:
        article_text_co = text_co
        comments_frame = tk.Frame(root, bd=2, relief="sunken")
        comments_display = scrolledtext.ScrolledText(comments_frame, width=50, height=10, font=("Arial", 12))
        comments_display.insert("end", article_text_co)
        comments_display.pack(expand=True, fill="both")
        comments_frame.pack(side="left", padx=10, pady=10, expand=True, fill="both")

    # Vytvoření tlačítek
    button_frame = tk.Frame(root)


    next_button = tk.Button(button_frame, text="Další článek")
    next_button.pack(side="left", padx=5, pady=5)
    write_button = tk.Button(button_frame, text="Napsat článek")
    write_button.pack(side="left", padx=5, pady=5)
    comment_button = tk.Button(button_frame, text="Napsat komentář")
    comment_button.pack(side="left", padx=5, pady=5)
    exit_button = tk.Button(button_frame, text="Ukončit", command=root.destroy)
    exit_button.pack(side="left", padx=5, pady=5)
    button_frame.pack(side="bottom", pady=10)

    def cre_cl():
        """
        Reaguje na zmáčknutí tlačítka Napsat článek
        :return:
        """
        clanek.cl_run(s,jm)

    write_button.configure(command=cre_cl)

    def cre_ko():
        """
        Reaguje na zmáčknutí tlačítka Napsat komentář
        :return:
        """
        komentar.run_co(s,jm,id_cl)

    comment_button.configure(command=cre_ko)

    def novy_clanek():
        """
        Reaguje na zmáčknutí tlačítka Další článek
        :return:
        """
        root.destroy()  # zničí existující okno aplikace
        aplik(s, jm)  # vytvoří nové okno aplikace

    next_button.configure(command=novy_clanek)

    root.mainloop()