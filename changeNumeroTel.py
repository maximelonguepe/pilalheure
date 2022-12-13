from tkinter import Toplevel, Label, Entry, Button


def changerNumeroTelView(menu):
    change_tel = Toplevel(menu)
    change_tel.title("Changer numéro téléphone")
    change_tel.geometry("480x320")
    text_font = ("Boulder", 20, 'bold')

    premier_numero = Label(change_tel, text=0, font=text_font)
    premier_numero.place(relx=0, rely=0.3)
    button_plus_premier_numero = Button(change_tel, text="+", width=3, height=4)
    button_plus_premier_numero.place(relx=0, rely=0.1)
    button_moins_premier_numero = Button(change_tel, text="-", width=3, height=4)
    button_moins_premier_numero.place(relx=0, rely=0.42)

    deuxieme_numero = Label(change_tel, text=0, font=text_font)
    deuxieme_numero.place(relx=0.1, rely=0.3)
    button_plus_deuxieme_numero = Button(change_tel, text="+", width=3, height=4)
    button_plus_deuxieme_numero.place(relx=0.1, rely=0.1)
    button_moins_deuxieme_numero = Button(change_tel, text="-", width=3, height=4)
    button_moins_deuxieme_numero.place(relx=0.1, rely=0.42)

    troisieme_numero = Label(change_tel, text=0, font=text_font)
    troisieme_numero.place(relx=0.2, rely=0.3)
    button_plus_troisieme_numero = Button(change_tel, text="+", width=3, height=4)
    button_plus_troisieme_numero.place(relx=0.2, rely=0.1)
    button_moins_troisieme_numero = Button(change_tel, text="-", width=3, height=4)
    button_moins_troisieme_numero.place(relx=0.2, rely=0.42)

    quatrieme_numero = Label(change_tel, text=0, font=text_font)
    quatrieme_numero.place(relx=0.3, rely=0.3)
    button_plus_quatrieme_numero = Button(change_tel, text="+", width=3, height=4)
    button_plus_quatrieme_numero.place(relx=0.3, rely=0.1)
    button_moins_quatrieme_numero = Button(change_tel, text="-", width=3, height=4)
    button_moins_quatrieme_numero.place(relx=0.3, rely=0.42)

    cinquieme_numero = Label(change_tel, text=0, font=text_font)
    cinquieme_numero.place(relx=0.4, rely=0.3)
    button_plus_cinquieme_numero = Button(change_tel, text="+", width=3, height=4)
    button_plus_cinquieme_numero.place(relx=0.4, rely=0.1)
    button_moins_cinquieme_numero = Button(change_tel, text="-", width=3, height=4)
    button_moins_cinquieme_numero.place(relx=0.4, rely=0.42)

    sixieme_numero = Label(change_tel, text=0, font=text_font)
    sixieme_numero.place(relx=0.5, rely=0.3)
    button_plus_sixieme_numero = Button(change_tel, text="+", width=3, height=4)
    button_plus_sixieme_numero.place(relx=0.5, rely=0.1)
    button_moins_sixieme_numero = Button(change_tel, text="-", width=3, height=4)
    button_moins_sixieme_numero.place(relx=0.5, rely=0.42)

    septieme_numero = Label(change_tel, text=0, font=text_font)
    septieme_numero.place(relx=0.6, rely=0.3)
    button_plus_septieme_numero = Button(change_tel, text="+", width=3, height=4)
    button_plus_septieme_numero.place(relx=0.6, rely=0.1)
    button_moins_septieme_numero = Button(change_tel, text="-", width=3, height=4)
    button_moins_septieme_numero.place(relx=0.6, rely=0.42)

    huitieme_numero = Label(change_tel, text=0, font=text_font)
    huitieme_numero.place(relx=0.7, rely=0.3)
    button_plus_huitieme_numero = Button(change_tel, text="+", width=3, height=4)
    button_plus_huitieme_numero.place(relx=0.7, rely=0.1)
    button_moins_huitieme_numero = Button(change_tel, text="-", width=3, height=4)
    button_moins_huitieme_numero.place(relx=0.7, rely=0.42)

    neuvieme_numero = Label(change_tel, text=0, font=text_font)
    neuvieme_numero.place(relx=0.8, rely=0.3)
    button_plus_neuvieme_numero = Button(change_tel, text="+", width=3, height=4)
    button_plus_neuvieme_numero.place(relx=0.8, rely=0.1)
    button_moins_neuvieme_numero = Button(change_tel, text="-", width=3, height=4)
    button_moins_neuvieme_numero.place(relx=0.8, rely=0.42)

    dizieme_numero = Label(change_tel, text=0, font=text_font)
    dizieme_numero.place(relx=0.9, rely=0.3)
    button_plus_dizieme_numero = Button(change_tel, text="+", width=3, height=4)
    button_plus_dizieme_numero.place(relx=0.9, rely=0.1)
    button_moins_dizieme_numero = Button(change_tel, text="-", width=3, height=4)
    button_moins_dizieme_numero.place(relx=0.9, rely=0.42)

