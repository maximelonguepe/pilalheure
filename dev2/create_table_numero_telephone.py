import sqlite3
con = sqlite3.connect("../database.db")
cur = con.cursor()
cur.execute("CREATE TABLE numero_telephone(id INTEGER PRIMARY KEY AUTOINCREMENT,numero VARCHAR(10))")
