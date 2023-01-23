from tkinter import Label, Tk
import time
import menu
from threading import Thread
from database.rappel import get_rappel_hour
from utils.time_util import full_day_to_int
from hardware.buzzer import buzz_on,buzz_off

def thread_verifie_heure():
    while True:
        heure_rappel, minutes_rappel = get_rappel_hour()
        heur_reelle = int(time.strftime("%H"))
        minutes_reelles = int(time.strftime("%M"))
        jour_reel = time.strftime("%A")
        day = full_day_to_int(jour_reel)
        if heure_rappel == heur_reelle and minutes_rappel == minutes_reelles:
            time.sleep(1)
            while True:
                buzz_on()
                time.sleep(1)
                buzz_off()
                time.sleep(1)

        time.sleep(60)


def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(1000, digital_clock)


if __name__ == '__main__':
    app_window = Tk()
    app_window.title("Digital Clock")
    app_window.geometry("480x320")
    text_font = ("Boulder", 67, 'bold')
    border_width = 25
    label = Label(app_window, font=text_font, bd=border_width)
    label.bind("<Button-1>", lambda e: menu.menuView(app_window))
    label.grid(row=0, column=1)
    digital_clock()
    thread = Thread(target=thread_verifie_heure)
    thread.start()
    # windowUtils.unclose_window(app_window)
    app_window.mainloop()
