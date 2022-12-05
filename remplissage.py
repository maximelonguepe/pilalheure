from tkinter import Toplevel, Label, Button
from database.prise import getNomsMedicamentsPasRemplis
from scanner import scannerMedicament

page = 0


def page_precedente():
    global page
    page -= 1


def page_suivante():
    global page
    page += 1


def updateList(label, window, btnbas, btnhaut):
    global page
    liste_medicaments = getNomsMedicamentsPasRemplis()
    if len(liste_medicaments) <= 5:
        btnbas.place_forget()
        btnhaut.place_forget()
        buffer = ""
        for medicament in liste_medicaments:
            string1 = medicament[:40]
            if len(medicament) > 40:
                string1 += "..."
            buffer += "-" + string1 + "\n"
        label.config(text=buffer)
        label.after(200, lambda: updateList(label, window, btnbas, btnhaut))
    else:
        buffer = ""

        if (page * 5) + 5 <= len(liste_medicaments):
            end = (page * 5) + 5
        else:
            end = len(liste_medicaments)
        for i in range(page * 5, end):
            medicament = liste_medicaments[i]
            string1 = medicament[:40]
            if len(medicament) > 40:
                string1 += "..."
            buffer += "-" + string1 + "\n"
        label.config(text=buffer)
        label.after(200, lambda: updateList(label, window, btnbas, btnhaut))
        if page >= int(len(liste_medicaments) / 5):
            btnbas.place_forget()
        else:
            btnbas.place(relx=0.5, rely=0.7)
        if page == 0:
            btnhaut.place_forget()
        else:
            btnhaut.place(relx=0, rely=0.7)


def printok():
    print("ok")


def remplissageView(menu_view):
    remplissage = Toplevel(menu_view)
    remplissage.geometry("480x320")
    list_font = ("Boulder", 12, 'bold')
    remplissage.title("Remplissage pilulier")
    titre_font = ("Boulder", 18, 'bold')
    label_titre = Label(remplissage, text="Liste des médicaments à remplir :", font=titre_font)
    label_titre.place(relx=0, rely=0)
    label_nom_medicaments = Label(remplissage, background="#d9d9d9", font=list_font)
    label_nom_medicaments.place(relx=0, rely=0.2)
    btnhaut = Button(remplissage, text="H", command=lambda: page_precedente(), width=30)
    btnhaut.place(relx=0, rely=0.7)
    btnbas = Button(remplissage, text="B", command=lambda: page_suivante(), width=30)
    btnbas.place(relx=0.5, rely=0.7)
    updateList(label_nom_medicaments, remplissage, btnbas, btnhaut)
    btn_scanner = Button(remplissage, text="Scanner", command=lambda: scannerMedicament(remplissage, 2), width=60)
    btn_scanner.place(relx=0, rely=0.8)
    remplissage.mainloop()
