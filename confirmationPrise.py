from tkinter import Toplevel, Label, Button
from clock import prise


def confirmer_vue_prise(clock):
    confirmer_prise = Toplevel(clock)
    confirmer_prise.title("Confirmer la prise")
    confirmer_prise.geometry("480x320")
    text_font = ("Boulder", 15, 'bold')

    print(prise)

    confirmer_prise.mainloop()
