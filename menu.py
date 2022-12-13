from tkinter import Button, Toplevel
from remplissage import remplissageView
import scanner
import changeHeurePrise

page = 0


def precedent():
    global page
    page = page - 1
    print(page)


def suivant():
    global page
    page += 1
    print(page)


def menuView(app_window):
    global menu_widow
    menu_widow = Toplevel(app_window)
    menu_widow.title("Menu")
    menu_widow.geometry("480x320")
    button_width = 30
    button_height = 5
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
    btn3.place(relx=0, rely=0.3)
    btn4 = Button(menu_widow, text="Remplissage", background=background_color, width=button_width, height=button_height,
                  command=lambda: remplissageView(menu_widow))
    btn4.place(relx=0.5, rely=0.3)

    btnPrecedent = Button(menu_widow, text="<-", background=background_color, width=button_width, height=3,
                          command=lambda: precedent())
    btnPrecedent.place(relx=0, rely=0.6)

    btnSuivant = Button(menu_widow, text="->", background=background_color, width=button_width, height=3,
                        command=lambda: suivant())
    btnSuivant.place(relx=0.5, rely=0.6)

    menu_widow.mainloop()
