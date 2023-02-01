from tkinter import Toplevel, Label, Entry, Button

import database.prise as prise
from jourPrise import jourPriseView
from suppressionMedicament import supprimer_medicament_view
from remplissageUnMedicament import remplir_un_medicament


def versJoursPrise(resultat_scan, scan, parcours):
    # TODO : gerer les erreurs
    # TODO : si il y a déjà le médicament empecher lenregistrement

    # parcours = 0 si modifier les jours de prise
    if parcours == 0:
        nom_medicament, id_medicament, code_retour = prise.getPrise(resultat_scan.get())
        if code_retour == 200:
            jourPriseView(nom_medicament, scan, id_medicament, parcours)
        elif code_retour == 404:
            text_font = ("Boulder", 12, 'bold')
            label_erreur = Label(scan, text="Erreur le médicament n'est pas enregistré", font=text_font)
            label_erreur.grid(row=3, column=1)
            label_erreur.config(fg="red")

    # parcours = 1 si enregistrer nouveau medicament
    elif parcours == 1:
        nom_medicament, id_medicament = prise.getMedicament(resultat_scan.get())
        jourPriseView(nom_medicament, scan, id_medicament, parcours)

    # parcours = 2 pour remplir une case avec un medicament
    elif parcours == 2:
        est_rempli, code_retour = prise.getSiRempliOuNon(resultat_scan.get())
        # si aucun médicament n'a été trouvé
        if code_retour == 404:
            text_font = ("Boulder", 12, 'bold')
            label_erreur = Label(scan, text="Erreur le médicament n'est pas enregistré", font=text_font)
            label_erreur.grid(row=3, column=1)
            label_erreur.config(fg="red")

        # si le médicament est déjà rempli
        elif est_rempli == 1:
            text_font = ("Boulder", 12, 'bold')
            label_erreur = Label(scan, text="Erreur le médicament a déjà été rempli", font=text_font)
            label_erreur.grid(row=3, column=1)
            label_erreur.config(fg="red")

        # TODO : si le médicament n'est pas rempli alors on modifie le champ en base
        elif est_rempli == 0:
            nom_medicament, id_medicament, code_retour = prise.getPrise(resultat_scan.get())
            remplir_un_medicament(scan, nom_medicament, id_medicament, code_retour)
    # supprimer medicament de la liste des prises
    elif parcours == 3:
        nom_medicament, id_medicament, code_retour = prise.getPrise(resultat_scan.get())
        if code_retour == 404:
            text_font = ("Boulder", 12, 'bold')
            label_erreur = Label(scan, text="Erreur le médicament n'est pas enregistré", font=text_font)
            label_erreur.grid(row=3, column=1)
            label_erreur.config(fg="red")
        else:
            supprimer_medicament_view(scan, nom_medicament, id_medicament)


def quit_scanner():
    scan.destroy()


# TODO refactoriser le code pour mettre des place au lieu des grid
def scannerMedicament(menu, parcours):
    global scan
    scan = Toplevel(menu)
    scan.title("Scanner medicament")
    scan.geometry("480x320")
    text_font = ("Boulder", 15, 'bold')
    border_width = 25
    label_scan = Label(scan, text="Veuillez scanner le médicament", font=text_font, bd=border_width)
    label_scan.place(rely=0, relx=0)
    entry = Entry(scan, width=40)
    entry.focus_set()
    entry.place(relx=0.3, rely=0.2)
    btn = Button(scan, text="Ok", width=40, height=5, command=lambda: versJoursPrise(entry, scan, parcours))
    btn.place(relx=0.2, rely=0.4)
    btn_cancel = Button(scan, text="Annuler la saisie ", width=40, height=5,command=quit_scanner)
    btn_cancel.place(rely=0.7, relx=0.2)
    scan.mainloop()
