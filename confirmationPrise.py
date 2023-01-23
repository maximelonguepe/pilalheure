from tkinter import Toplevel


def confirmer_vue_prise(clock):
    confirmer_prise = Toplevel(clock)
    confirmer_prise.title("Confirmer la prise")
    confirmer_prise.geometry("480x320")
    text_font = ("Boulder", 15, 'bold')

    confirmer_prise.mainloop()
