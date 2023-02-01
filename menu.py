from tkinter import Button, Toplevel

import changeHeurePrise
import scanner
from changeNumeroTel import changerNumeroTelView
from remplissage import remplissageView

page = 0
menu_widow = 1


def precedent():
    global page
    page = page - 1


def suivant():
    global page
    page += 1


def affichage_page(btn, btn2, btn3, btn4, btn_precedent, btn_suivant):
    global page
    global menu_widow

    if page == 0:
        btn.config(text="Changer heure de prise")
        btn.config(command=lambda: changeHeurePrise.changeHeureView(menu_widow))
        btn2.config(text="Ajouter un medicament")
        btn2.config(command=lambda: scanner.scannerMedicament(menu_widow, 1))
        btn_precedent.place_forget()
        btn_suivant.place(relx=0.5, rely=0.5)

    elif page == 1:
        btn.config(text="Changer numéro de tel")
        btn.config(command=lambda: changerNumeroTelView(menu_widow))
        btn_suivant.place_forget()
        btn2.config(text="Supprimer médicament")
        btn2.config(command=lambda: scanner.scannerMedicament(menu_widow, 3))
        btn_precedent.place(relx=0, rely=0.5)


def precedent_et_affiche(btn, btn2, btn3, btn4, btn_precedent, btn_suivant):
    precedent()
    affichage_page(btn, btn2, btn3, btn4, btn_precedent, btn_suivant)


def suivant_et_affiche(btn, btn2, btn3, btn4, btn_precedent, btn_suivant):
    suivant()
    affichage_page(btn, btn2, btn3, btn4, btn_precedent, btn_suivant)

def close_widow():
    global menu_widow
    menu_widow.destroy()

def menuView(app_window):
    global menu_widow
    menu_widow = Toplevel(app_window)
    menu_widow.title("Menu")
    menu_widow.geometry("480x320")
    button_width = 30
    button_height = 4
    background_color = "#d9d9d9"
    btn = Button(menu_widow, text="Changer heure de prise",
                 command=lambda: changeHeurePrise.changeHeureView(menu_widow), width=button_width, height=button_height,
                 background=background_color)
    btn.place(relx=0, rely=0)
    btn2 = Button(menu_widow, text="Ajouter un medicament", command=lambda: scanner.scannerMedicament(menu_widow, 1),
                  width=button_width, height=button_height, background=background_color)
    btn2.place(relx=0.5, rely=0)
    btn3 = Button(menu_widow, text="Modifer les jours de prise",
                  command=lambda: scanner.scannerMedicament(menu_widow, 0), width=button_width, height=button_height,
                  background=background_color)
    btn3.place(relx=0, rely=0.25)
    btn4 = Button(menu_widow, text="Remplissage", background=background_color, width=button_width, height=button_height,
                  command=lambda: remplissageView(menu_widow))
    btn4.place(relx=0.5, rely=0.25)

    btn_precedent = Button(menu_widow, text="<-", background=background_color, width=button_width, height=3,
                           command=lambda: precedent_et_affiche(btn, btn2, btn3, btn4, btn_precedent, btn_suivant))

    btn_suivant = Button(menu_widow, text="->", background=background_color, width=button_width, height=3,
                         command=lambda: suivant_et_affiche(btn, btn2, btn3, btn4, btn_precedent, btn_suivant))
    btn_suivant.place(relx=0.5, rely=0.5)
    btn_close = Button(menu_widow, text="Fermer", background=background_color, width=button_width, height=3,
                       command=lambda: close_widow())
    btn_close.place(relx=0, rely=0.7)
    menu_widow.mainloop()
