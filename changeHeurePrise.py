from tkinter import Toplevel, Label, Entry, Button
from database.rappel import get_rappel_hour, update_heure_rappel


def plus(label, max):
    time = int(label.cget('text'))
    if time == max:
        time = 0
    else:
        time += 1
    time_str = str(time)
    zero = ""
    if len(time_str) == 1:
        zero = "0"
    label.config(text=zero + str(time))


def update_heure_rappel_and_close(changeHeure, heure, minutes):
    update_heure_rappel(heure, minutes)
    changeHeure.destroy()


def moins(label, max):
    time = int(label.cget('text'))
    if time == 0:
        time = max
    else:
        time -= 1
    time_str = str(time)
    zero = ""
    if len(time_str) == 1:
        zero = "0"
    label.config(text=zero + str(time))


def changeHeureView(menu):
    changeHeure = Toplevel(menu)
    changeHeure.title("Changer heure rappel")
    changeHeure.geometry("480x320")
    heure, minutes = get_rappel_hour()
    text_font = ("Boulder", 20, 'bold')
    button_moins_heure = Button(changeHeure, text="-", font=text_font, width=5, command=lambda: moins(heure_label, 23))
    button_moins_heure.place(relx=.25)
    heure_label = Label(changeHeure, text=heure, font=text_font)
    heure_label.place(relx=.5, rely=.03)
    button_plus_heure = Button(changeHeure, text="+", font=text_font, width=5, command=lambda: plus(heure_label, 23))
    button_plus_heure.place(relx=.6)

    button_moins_minutes = Button(changeHeure, text="-", font=text_font, width=5,
                                  command=lambda: moins(minutes_label, 59))
    button_moins_minutes.place(relx=.25, rely=.5)
    minutes_label = Label(changeHeure, text=minutes, font=text_font)
    minutes_label.place(relx=.5, rely=.53)
    button_plus_minutes = Button(changeHeure, text="+", font=text_font, width=5,
                                 command=lambda: plus(minutes_label, 59))
    button_plus_minutes.place(relx=.6, rely=.5)
    button_ok = Button(changeHeure, text="Ok", width=30*2, height=5,
                       command=lambda: update_heure_rappel_and_close(changeHeure, int(heure_label.cget('text')),
                                                                     int(minutes_label.cget('text'))))
    button_ok.place(relx=0, rely=.7)
    changeHeure.mainloop()
