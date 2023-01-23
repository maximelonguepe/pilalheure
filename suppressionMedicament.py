from tkinter import Toplevel, Label, Button

from database.prise import suppression_prise


# Fait appel a une fonction du package database pour supprimer un medicament et ferme les fenetres
def supprimer_medicament(id_medicament, fenetre, scanner):
    suppression_prise(id_medicament)
    fermer_fenetre(fenetre, scanner)


# Permet de fermer la fenetre de scan et de suppression
def fermer_fenetre(suppression_medicament, scanner):
    suppression_medicament.destroy()
    fermer_fenetre_scanner(scanner)


# Permet de fermer la fenetre de scan
def fermer_fenetre_scanner(scanner):
    scanner.destroy()


# Affichage utilisateur avec une demande de confirmation de suppression du medicament
def supprimer_medicament_view(scanner, nom_medicament, id_medicament):
    suppression_medicament = Toplevel(scanner)
    suppression_medicament.title("Supprimer medicament")
    suppression_medicament.geometry("480x320")
    text_font = ("Boulder", 15, 'bold')
    label_suppression = Label(suppression_medicament, text="Supprimer le medicament ?",
                              font=text_font)
    label_suppression.place(rely=0, relx=0)
    label_nom_medicament = Label(suppression_medicament, text=nom_medicament,
                                 font=text_font)
    label_nom_medicament.place(relx=0, rely=0.2)
    bouton_oui = Button(suppression_medicament, text="Oui", width=25, height=7,
                        command=lambda: supprimer_medicament(id_medicament, suppression_medicament, scanner))
    bouton_oui.place(rely=0.4, relx=0)
    bouton_non = Button(suppression_medicament, text="Non", width=25, height=7,
                        command=lambda: fermer_fenetre(suppression_medicament, scanner))
    bouton_non.place(rely=0.4, relx=0.6)

    suppression_medicament.mainloop()
