from tkinter import Toplevel, Label, Button
from database.prise import getJoursPrise
from database.prise import remplirPilulierMedicament


def cache_jours_inutile(id_medicament, tableau_labels,jours):
    position_x = 0
    for i in range(len(jours)):
        if jours[i] == 1:
            tableau_labels[i].place(relx=position_x, rely=0.2)
            position_x = position_x + 0.1428571428571429


def enregister_prise_medicament(id_medicament, remplissage_un_medicament, scanner):
    remplirPilulierMedicament(id_medicament)
    remplissage_un_medicament.destroy()
    scanner.destroy()


def remplir_un_medicament(scanner, nom_medicament, id_medicament, code_retour):
    remplissage_un_medicament = Toplevel(scanner)
    remplissage_un_medicament.title("Remplir un medicament")
    remplissage_un_medicament.geometry("480x320")
    text_font = ("Boulder", 10, 'bold')
    tableau_labels = []
    label_nom_medicament = Label(remplissage_un_medicament, text=nom_medicament, font=text_font)
    label_nom_medicament.place(rely=0, relx=0)
    label_liste_jours_a_remplir = Label(remplissage_un_medicament, text="Jours à remplir pour ce médicament ",
                                        font=text_font)
    label_liste_jours_a_remplir.place(rely=0.1, relx=0)

    label_lundi = Label(remplissage_un_medicament, text="Lundi", font=text_font)
    label_mardi = Label(remplissage_un_medicament, text="Mardi", font=text_font)
    label_mercredi = Label(remplissage_un_medicament, text="Mercredi", font=text_font)
    label_jeudi = Label(remplissage_un_medicament, text="Jeudi", font=text_font)
    label_vendredi = Label(remplissage_un_medicament, text="Vendredi", font=text_font)
    label_samedi = Label(remplissage_un_medicament, text="Samedi", font=text_font)
    label_dimanche = Label(remplissage_un_medicament, text="Dimanche", font=text_font)

    tableau_labels.append(label_lundi)
    tableau_labels.append(label_mardi)
    tableau_labels.append(label_mercredi)
    tableau_labels.append(label_jeudi)
    tableau_labels.append(label_vendredi)
    tableau_labels.append(label_samedi)
    tableau_labels.append(label_dimanche)

    button_ok = Button(remplissage_un_medicament, text="Remplissage terminé",
                       command=lambda: enregister_prise_medicament(id_medicament, remplissage_un_medicament, scanner),
                       font=text_font, width=58, height=5)
    button_ok.place(relx=0, rely=0.5)
    tableau_jours = getJoursPrise(id_medicament)
    cache_jours_inutile(id_medicament, tableau_labels, tableau_jours)
    remplissage_un_medicament.mainloop()
