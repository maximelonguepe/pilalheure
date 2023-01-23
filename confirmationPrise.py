import time
from threading import Thread
from tkinter import Toplevel, Button

from hardware.buzzer import *

quit_window = 0


def thread_bippe():
    global quit_window
    while not quit_window:
        global quit_window
        buzz_on()
        time.sleep(1)
        buzz_off()
        time.sleep(1)


def close_and_quit_thread(confirmer_prise):
    confirmer_prise.destroy()
    global quit_window
    quit_window = True


def confirmer_vue_prise(clock):
    confirmer_prise = Toplevel(clock)
    confirmer_prise.title("Confirmer la prise")
    confirmer_prise.geometry("480x320")
    text_font = ("Boulder", 15, 'bold')
    bouton_confirm = Button(confirmer_prise, text="Confirmer la prise",
                            command=lambda: close_and_quit_thread())
    bouton_confirm.place(relx=0, rely=0)
    thread = Thread(target=thread_bippe())
    thread.start()

    confirmer_prise.mainloop()
