import sqlite3
con = sqlite3.connect("../database.db")
cur = con.cursor()
cur.execute("CREATE TABLE medicaments(id,cip, cip_ucd, nom_court)")

