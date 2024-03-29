from tkinter import Toplevel, Label, Button
from database.telephone import get_numero_telephone, update_numero_telephone, insert_numero_telphone


def init_number(numero, premier_numero, deuxieme_numero, troisieme_numero, quatrieme_numero, cinquieme_numero,
                sixieme_numero, septieme_numero, huitieme_numero, neuvieme_numero, dizieme_numero):
    liste_caracters_telephone = list(numero)
    premier_numero.config(text=liste_caracters_telephone[0])
    deuxieme_numero.config(text=liste_caracters_telephone[1])
    troisieme_numero.config(text=liste_caracters_telephone[2])
    quatrieme_numero.config(text=liste_caracters_telephone[3])
    cinquieme_numero.config(text=liste_caracters_telephone[4])
    sixieme_numero.config(text=liste_caracters_telephone[5])
    septieme_numero.config(text=liste_caracters_telephone[6])
    huitieme_numero.config(text=liste_caracters_telephone[7])
    neuvieme_numero.config(text=liste_caracters_telephone[8])
    dizieme_numero.config(text=liste_caracters_telephone[9])


def plus(label):
    numero = int(label.cget('text'))
    if numero == 9:
        numero = 0
    else:
        numero += 1
    label.config(text=str(numero))


def moins(label):
    numero = int(label.cget('text'))
    if numero == 0:
        numero = 9
    else:
        numero = numero - 1
    label.config(text=str(numero))


def enregistre_changement(code_erreur, numero, nouveau_numero):
    if code_erreur == 404:
        insert_numero_telphone(nouveau_numero)
    elif code_erreur == 200:
        if numero != nouveau_numero:
            update_numero_telephone(nouveau_numero)


def construit_nouveau_numero(premier_numero, deuxieme_numero, troisieme_numero, quatrieme_numero, cinquieme_numero,
                             sixieme_numero, septieme_numero, huitieme_numero, neuvieme_numero, dizieme_numero):
    return str(premier_numero.cget('text')) + str(deuxieme_numero.cget('text')) + str(troisieme_numero.cget(
        'text')) + str(quatrieme_numero.cget('text')) + str(cinquieme_numero.cget('text')) + str(sixieme_numero.cget(
        'text')) + str(septieme_numero.cget('text')) + str(huitieme_numero.cget('text')) + str(neuvieme_numero.cget(
        'text')) + str(dizieme_numero.cget('text'))


def enregistre(change_tel, premier_numero, deuxieme_numero, troisieme_numero, quatrieme_numero, cinquieme_numero,
               sixieme_numero, septieme_numero, huitieme_numero, neuvieme_numero, dizieme_numero, code_erreur, numero):
    nouveau_numero = construit_nouveau_numero(premier_numero, deuxieme_numero, troisieme_numero, quatrieme_numero,
                                              cinquieme_numero,
                                              sixieme_numero, septieme_numero, huitieme_numero, neuvieme_numero,
                                              dizieme_numero)
    enregistre_changement(code_erreur, numero, nouveau_numero)
    change_tel.destroy()

def changerNumeroTelView(menu):
    change_tel = Toplevel(menu)
    change_tel.title("Changer numéro téléphone")
    change_tel.geometry("480x320")
    text_font = ("Boulder", 20, 'bold')

    premier_numero = Label(change_tel, text=0, font=text_font)
    premier_numero.place(relx=0, rely=0.3)
    button_plus_premier_numero = Button(change_tel, text="+", width=3, height=4, command=lambda: plus(premier_numero))
    button_plus_premier_numero.place(relx=0, rely=0.0)
    button_moins_premier_numero = Button(change_tel, text="-", width=3, height=4, command=lambda: moins(premier_numero))
    button_moins_premier_numero.place(relx=0, rely=0.42)

    deuxieme_numero = Label(change_tel, text=0, font=text_font)
    deuxieme_numero.place(relx=0.1, rely=0.3)
    button_plus_deuxieme_numero = Button(change_tel, text="+", width=3, height=4, command=lambda: plus(deuxieme_numero))
    button_plus_deuxieme_numero.place(relx=0.1, rely=0)
    button_moins_deuxieme_numero = Button(change_tel, text="-", width=3, height=4,
                                          command=lambda: moins(deuxieme_numero))
    button_moins_deuxieme_numero.place(relx=0.1, rely=0.42)

    troisieme_numero = Label(change_tel, text=0, font=text_font)
    troisieme_numero.place(relx=0.2, rely=0.3)
    button_plus_troisieme_numero = Button(change_tel, text="+", width=3, height=4,
                                          command=lambda: plus(troisieme_numero))
    button_plus_troisieme_numero.place(relx=0.2, rely=0)
    button_moins_troisieme_numero = Button(change_tel, text="-", width=3, height=4,
                                           command=lambda: moins(troisieme_numero))
    button_moins_troisieme_numero.place(relx=0.2, rely=0.42)

    quatrieme_numero = Label(change_tel, text=0, font=text_font)
    quatrieme_numero.place(relx=0.3, rely=0.3)
    button_plus_quatrieme_numero = Button(change_tel, text="+", width=3, height=4,
                                          command=lambda: plus(quatrieme_numero))
    button_plus_quatrieme_numero.place(relx=0.3, rely=0)
    button_moins_quatrieme_numero = Button(change_tel, text="-", width=3, height=4,
                                           command=lambda: moins(quatrieme_numero))
    button_moins_quatrieme_numero.place(relx=0.3, rely=0.42)

    cinquieme_numero = Label(change_tel, text=0, font=text_font)
    cinquieme_numero.place(relx=0.4, rely=0.3)
    button_plus_cinquieme_numero = Button(change_tel, text="+", width=3, height=4,
                                          command=lambda: plus(cinquieme_numero))
    button_plus_cinquieme_numero.place(relx=0.4, rely=0)
    button_moins_cinquieme_numero = Button(change_tel, text="-", width=3, height=4,
                                           command=lambda: moins(cinquieme_numero))
    button_moins_cinquieme_numero.place(relx=0.4, rely=0.42)

    sixieme_numero = Label(change_tel, text=0, font=text_font)
    sixieme_numero.place(relx=0.5, rely=0.3)
    button_plus_sixieme_numero = Button(change_tel, text="+", width=3, height=4, command=lambda: plus(sixieme_numero))
    button_plus_sixieme_numero.place(relx=0.5, rely=0)
    button_moins_sixieme_numero = Button(change_tel, text="-", width=3, height=4, command=lambda: moins(sixieme_numero))
    button_moins_sixieme_numero.place(relx=0.5, rely=0.42)

    septieme_numero = Label(change_tel, text=0, font=text_font)
    septieme_numero.place(relx=0.6, rely=0.3)
    button_plus_septieme_numero = Button(change_tel, text="+", width=3, height=4, command=lambda: plus(septieme_numero))
    button_plus_septieme_numero.place(relx=0.6, rely=0)
    button_moins_septieme_numero = Button(change_tel, text="-", width=3, height=4,
                                          command=lambda: moins(septieme_numero))
    button_moins_septieme_numero.place(relx=0.6, rely=0.42)

    huitieme_numero = Label(change_tel, text=0, font=text_font)
    huitieme_numero.place(relx=0.7, rely=0.3)
    button_plus_huitieme_numero = Button(change_tel, text="+", width=3, height=4, command=lambda: plus(huitieme_numero))
    button_plus_huitieme_numero.place(relx=0.7, rely=0)
    button_moins_huitieme_numero = Button(change_tel, text="-", width=3, height=4,
                                          command=lambda: moins(huitieme_numero))
    button_moins_huitieme_numero.place(relx=0.7, rely=0.42)

    neuvieme_numero = Label(change_tel, text=0, font=text_font)
    neuvieme_numero.place(relx=0.8, rely=0.3)
    button_plus_neuvieme_numero = Button(change_tel, text="+", width=3, height=4, command=lambda: plus(neuvieme_numero))
    button_plus_neuvieme_numero.place(relx=0.8, rely=0)
    button_moins_neuvieme_numero = Button(change_tel, text="-", width=3, height=4,
                                          command=lambda: moins(neuvieme_numero))
    button_moins_neuvieme_numero.place(relx=0.8, rely=0.42)

    dizieme_numero = Label(change_tel, text=0, font=text_font)
    dizieme_numero.place(relx=0.9, rely=0.3)
    button_plus_dizieme_numero = Button(change_tel, text="+", width=3, height=4, command=lambda: plus(dizieme_numero))
    button_plus_dizieme_numero.place(relx=0.9, rely=0)
    button_moins_dizieme_numero = Button(change_tel, text="-", width=3, height=4, command=lambda: moins(dizieme_numero))
    button_moins_dizieme_numero.place(relx=0.9, rely=0.42)

    numero, code = get_numero_telephone()
    if code != 404:
        init_number(numero, premier_numero, deuxieme_numero, troisieme_numero, quatrieme_numero, cinquieme_numero,
                    sixieme_numero, septieme_numero, huitieme_numero, neuvieme_numero, dizieme_numero)


    button_ok = Button(change_tel, text="OK", width=70, height=3, command=lambda: enregistre(change_tel,
                                                                                             premier_numero,
                                                                                             deuxieme_numero,
                                                                                             troisieme_numero,
                                                                                             quatrieme_numero,
                                                                                             cinquieme_numero,
                                                                                             sixieme_numero,
                                                                                             septieme_numero,
                                                                                             huitieme_numero,
                                                                                             neuvieme_numero,
                                                                                             dizieme_numero, code,
                                                                                             numero))
    button_ok.place(relx=0, rely=0.7)
