import time
from tkinter import Toplevel

from hardware.buzzer import *


def confirmer_vue_prise(clock, prise):
    confirmer_prise = Toplevel(clock)
    confirmer_prise.title("Confirmer la prise")
    confirmer_prise.geometry("480x320")
    text_font = ("Boulder", 15, 'bold')
    prise = False
    while prise == False:
        buzz_on()
        time.sleep(1)
        buzz_off()
        time.sleep(1)
    confirmer_prise.mainloop()
