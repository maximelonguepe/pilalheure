from tkinter import Toplevel, Label, Entry, Button
from jourPrise import jourPriseView
import database.prise as prise


def versJoursPrise(entry, scan, parcours):
    # TODO : a fixer
    # TODO : si il y a déjà le médicament empecher lenregistrement
    if parcours == 0:
        name, id_medicament = prise.getPrise(entry.get())
        jourPriseView(name, scan, id_medicament, parcours)

    elif parcours == 1:
        name, id_medicament = prise.getMedicament(entry.get())
        jourPriseView(name, scan, id_medicament, parcours)

    elif parcours == 2:
        est_rempli, code_retour = prise.getSiRempliOuNon(entry.get())
        if code_retour == 404:
            text_font = ("Boulder", 12, 'bold')
            label_erreur = Label(scan, text="Erreur le médicament n'est pas enregistré", font=text_font)
            label_erreur.grid(row=3, column=1)
            label_erreur.config(fg="red")
        elif est_rempli == 1:
            text_font = ("Boulder", 12, 'bold')
            label_erreur = Label(scan, text="Erreur le médicament a déjà été rempli", font=text_font)
            label_erreur.grid(row=3, column=1)
            label_erreur.config(fg="red")
        #elif est_rempli==0:

def quit_scanner():
    scan.destroy()


def scannerMedicament(menu, parcours):
    print()
    global scan
    scan = Toplevel(menu)
    scan.title("Scanner medicament")
    scan.geometry("480x320")
    text_font = ("Boulder", 20, 'bold')
    border_width = 25
    label_scan = Label(scan, text="Veuillez scanner le médicament", font=text_font, bd=border_width)
    label_scan.grid(row=0, column=1)
    entry = Entry(scan, width=40)
    entry.focus_set()
    entry.grid(row=1, column=1)
    btn = Button(scan, text="Ok", width=40, command=lambda: versJoursPrise(entry, scan, parcours))
    btn.grid(row=2, column=1)
    scan.mainloop()
