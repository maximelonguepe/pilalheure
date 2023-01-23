from tkinter import Toplevel, Label, Button
from clock import prise


def confirmer_vue_prise(clock, nom_medicament, id_medicament):
    confirmer_prise = Toplevel(clock)
    confirmer_prise.title("Supprimer medicament")
    confirmer_prise.geometry("480x320")
    text_font = ("Boulder", 15, 'bold')
    label_suppression = Label(confirmer_prise, text="Supprimer le medicament ?",
                              font=text_font)
    label_suppression.place(rely=0, relx=0)
    label_nom_medicament = Label(confirmer_prise, text=nom_medicament,
                                 font=text_font)
    label_nom_medicament.place(relx=0, rely=0.2)
    print(prise)

    confirmer_prise.mainloop()
