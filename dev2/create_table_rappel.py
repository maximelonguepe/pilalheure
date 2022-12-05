import sqlite3
con = sqlite3.connect("../database.db")
cur = con.cursor()
cur.execute("CREATE TABLE rappel(id,heure,minutes)")