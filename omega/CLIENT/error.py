import tkinter as tk

def err(text_err):
    """
    Výpíše chybové okno
    :param text_err: text erroru
    :return:
    """
    # vytvoření okna
    root = tk.Tk()
    root.title("Error")

    # vytvoření textu
    text = tk.Label(root, text=text_err)
    text.pack(pady=20) # nastavení mezery pod textem

    # vytvoření tlačítka
    button = tk.Button(root, text="OK", command=root.destroy)
    button.pack()

    # spuštění hlavní smyčky pro zobrazení okna
    root.mainloop()