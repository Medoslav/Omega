import tkinter as tk
import error
from CLIENT.methods import client_metody

def cl_run(s,jm):
    """
    Otevře okno na vytváření nového článku
    :param s: objekt připojí klienta
    :param jm: jméno klienta
    :return:
    """
    # Vytvoření nového okna
    text_window = tk.Tk()
    text_window.title("Zadejte text")

    # Vytvoření textového pole pro psaní textu
    text_entry = tk.Text(text_window, font=("Arial", 12), width=80, height=30)
    text_entry.pack(padx=10, pady=10)

    # Vytvoření tlačítek
    button_frame = tk.Frame(text_window)
    show_button = tk.Button(button_frame, text="Odeslat")
    show_button.pack(side="left", padx=5, pady=5)
    close_button = tk.Button(button_frame, text="Zavřít", command=text_window.destroy)
    close_button.pack(side="left", padx=5, pady=5)
    button_frame.pack(pady=10)

    def show_text():
        """
        Reaguje na stisk tlačítka Odeslat, zkontoluje jestli v poli je text a reaguje na výstup ze serveru
        :return:
        """
        text = text_entry.get("1.0", "end")
        if len(text) == 1:
            error.err("Nebyl zadán text.")
        if len(text) > 499:
            error.err("Příliš mnoho znaků.")
        x = client_metody.send_cla(s,jm,text)
        if x == "Y":
            error.err("Článek odeslán můžete zavřít okno.")
        if x == "N":
            error.err("Tento článek je opsanej, nekraď cizí práci!!!")


    show_button.configure(command=show_text)

    text_window.mainloop()