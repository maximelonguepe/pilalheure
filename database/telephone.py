import sqlite3


def get_numero_telephone():
    conn = sqlite3.connect('./database.db')
    cursor = conn.execute("SELECT numero from numero_telephone")
    numero_renseigne = 0
    code = 404
    for row in cursor:
        numero_renseigne = row[0]
        code = 200
    return numero_renseigne, code
