import time
from threading import Thread
from tkinter import Toplevel, Button

from hardware.buzzer import *


def thread_bippe():
    while True:
        buzz_on()
        time.sleep(1)
        buzz_off()
        time.sleep(1)


def confirmer_vue_prise(clock):
    confirmer_prise = Toplevel(clock)
    confirmer_prise.title("Confirmer la prise")
    confirmer_prise.geometry("480x320")
    text_font = ("Boulder", 15, 'bold')
    thread = Thread(target=thread_bippe())
    bouton_confirm = Button(confirmer_prise, text="Confirmer la prise",
                            command=lambda: confirmer_prise.destroy())
    bouton_confirm.place(relx=0,rely=0)
    confirmer_prise.mainloop()
