import time
from threading import Thread
from tkinter import Label, Tk, Button

import gpiozero

import menu
from database.rappel import get_rappel_hour
from hardware.buzzer import buzz_on, buzz_off
from hardware.multiple_servos import enclencher_servo_remplissage_haut, enclencher_servo_remplissage_bas, \
    enclencher_servo_prise_haut, enclencher_servo_prise_bas
from utils.time_util import full_day_to_int
from hardware.button import wait_for_press
from hardware.led import led_on,led_off
global app_window
global label
global button_ok_prise
global quit_window
global day


def thread_bippe():
    global quit_window
    global day
    thread_confirmation = Thread(target=thread_attente_bouton)
    thread_confirmation.start()
    while not quit_window:
        buzz_on()
        led_on()
        time.sleep(1)
        buzz_off()
        led_off()
        time.sleep(1)
    enclencher_servo_prise_haut(day)

    quit_window = False


def thread_attente_bouton():
    wait_for_press()
    confirmation_prise()


def thread_verifie_heure():
    while True:
        heure_rappel, minutes_rappel = get_rappel_hour()
        heur_reelle = int(time.strftime("%H"))
        minutes_reelles = int(time.strftime("%M"))
        jour_reel = time.strftime("%A")
        global day
        day = full_day_to_int(jour_reel)
        if heure_rappel == heur_reelle and minutes_rappel == minutes_reelles:
            label.place_forget()
            button_ok_prise.place(relx=0, rely=0.3)
            enclencher_servo_prise_bas(day)
            threadBippe = Thread(target=thread_bippe())
            threadBippe.start()
        time.sleep(60)


def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(1000, digital_clock)


def confirmation_prise():
    label.place(relx=0, rely=0)
    button_ok_prise.place_forget()
    global quit_window
    quit_window = True


if __name__ == '__main__':
    quit_window = False
    app_window = Tk()
    app_window.title("Digital Clock")
    app_window.geometry("480x320")
    text_font = ("Boulder", 67, 'bold')
    text_font2 = ("Boulder", 12, 'bold')
    border_width = 25
    label = Label(app_window, font=text_font, bd=border_width)
    label.bind("<Button-1>", lambda e: menu.menuView(app_window))
    label.place(relx=0, rely=0)
    button_ok_prise = Label(text="Confirmer la prise en appuyant sur le bouton",font=text_font2)
    digital_clock()
    thread = Thread(target=thread_verifie_heure)
    thread.start()

    # windowUtils.unclose_window(app_window)
    app_window.mainloop()
