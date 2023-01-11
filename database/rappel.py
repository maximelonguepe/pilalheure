import sqlite3

def get_rappel_hour():
    conn = sqlite3.connect('./database.db')
    cursor = conn.execute("SELECT heure,minutes FROM rappel")
    hour = 0
    minutes = 0
    for row in cursor:
        hour = row[0]
        minutes = row[1]
    return int(hour), int(minutes)


def update_heure_rappel(heure, minutes):
    conn = sqlite3.connect('./database.db')
    conn.execute("UPDATE rappel SET heure=" + str(heure) + ",minutes=" + str(minutes))
    conn.commit()
