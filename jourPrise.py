from tkinter import Toplevel, Button, Label
from database.prise import getJoursPrise, changeJoursPrise, ajoutPrise


def change_color(btn):
    if btn.cget('bg') == "#d9d9d9":
        btn.configure(background='green')
    else:
        btn.configure(background='#d9d9d9')


def init_colors(id_medicament, tableau_buttons):
    tab = getJoursPrise(id_medicament)
    for i in range(len(tab)):
        if tab[i] == 1:
            tableau_buttons[i].configure(background='green')


def est_Vert(btn):
    if btn.cget('bg') == 'green':
        return 1
    else:
        return 0


def change_jours_and_close(parcours, jourPrise, scan, id_medicament, btn, btn2, btn3, btn4, btn5, btn6, btn7):
    change_jours(parcours, id_medicament, btn, btn2, btn3, btn4, btn5, btn6, btn7)
    jourPrise.destroy()
    scan.destroy()


def change_jours(parcours, id_medicament, btn, btn2, btn3, btn4, btn5, btn6, btn7):
    lundi = est_Vert(btn)
    mardi = est_Vert(btn2)
    mercredi = est_Vert(btn3)
    jeudi = est_Vert(btn4)
    vendredi = est_Vert(btn5)
    samedi = est_Vert(btn6)
    dimanche = est_Vert(btn7)
    if parcours == 0:
        changeJoursPrise(id_medicament, lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche)
    else:
        ajoutPrise(id_medicament, lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche)


def jourPriseView(medicament, scan, id_medicament, parcours):
    text_font = ("Boulder", 20, 'bold')
    jourPrise = Toplevel(scan)
    jourPrise.geometry("480x320")
    jourPrise.title("Définir les jours de prise")
    tableau_buttons = []
    label = Label(jourPrise, text=medicament)
    label.grid(row=0, column=1, columnspan=5)
    btn = Button(jourPrise, text="Lundi", background="#d9d9d9", width=8, command=lambda: change_color(btn),
                 font=text_font)
    btn.grid(row=1, column=1, columnspan=2)
    btn2 = Button(jourPrise, text="Mardi", font=text_font, width=8, background="#d9d9d9",
                  command=lambda: change_color(btn2))
    btn2.grid(row=1, column=3, columnspan=2)
    btn3 = Button(jourPrise, text="Mercredi", font=text_font, width=8, background="#d9d9d9",
                  command=lambda: change_color(btn3))
    btn3.grid(row=1, column=5, columnspan=2)
    btn4 = Button(jourPrise, text="Jeudi", font=text_font, width=8, background="#d9d9d9",
                  command=lambda: change_color(btn4))
    btn4.grid(row=2, column=1, columnspan=2)
    btn5 = Button(jourPrise, text="Vendredi", font=text_font, width=8, background="#d9d9d9",
                  command=lambda: change_color(btn5))
    btn5.grid(row=2, column=3, columnspan=2)
    btn6 = Button(jourPrise, text="Samedi", font=text_font, width=8, background="#d9d9d9",
                  command=lambda: change_color(btn6))
    btn6.grid(row=3, column=1, columnspan=2)
    btn7 = Button(jourPrise, text="Dimanche", font=text_font, width=8, background="#d9d9d9",
                  command=lambda: change_color(btn7))
    btn7.grid(row=3, column=3, columnspan=2)

    btnOK = Button(jourPrise, text="Ok", width=60,
                   command=lambda: change_jours_and_close(parcours, scan, jourPrise, id_medicament, btn, btn2, btn3,
                                                          btn4,
                                                          btn5,
                                                          btn6,
                                                          btn7))

    btnOK.grid(row=4, column=1, columnspan=5)

    tableau_buttons.append(btn)
    tableau_buttons.append(btn2)
    tableau_buttons.append(btn3)
    tableau_buttons.append(btn4)
    tableau_buttons.append(btn5)
    tableau_buttons.append(btn6)
    tableau_buttons.append(btn7)

    if parcours == 0:
        init_colors(id_medicament, tableau_buttons)

    jourPrise.mainloop()
