import sqlite3

con = sqlite3.connect("../database.db")
cur = con.cursor()
cur.execute("CREATE TABLE prise(id_prise INTEGER PRIMARY KEY AUTOINCREMENT,id_medicament,rappel,lundi,mardi,mercredi,jeudi,vendredi,samedi,dimanche)")
