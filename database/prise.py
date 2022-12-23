import sqlite3


def getPrise(cip):
    conn = sqlite3.connect('./database.db')
    cursor = conn.execute(
        "SELECT medicaments.nom_court,cip,prise.id_medicament FROM medicaments,prise WHERE "
        "medicaments.id=prise.id_medicament AND medicaments.cip='" + cip + "'")
    name = ""
    id_medicament = 0
    code = 404
    for row in cursor:
        name = row[0]
        id_medicament = row[2]
        code = 200

    return name, id_medicament, code


def getMedicament(cip):
    conn = sqlite3.connect('./database.db')
    cursor = conn.execute(
        "SELECT nom_court,id FROM medicaments WHERE cip='" + cip + "'")

    name = ""
    id_medicament = 0
    for row in cursor:
        name = row[0]
        id_medicament = row[1]

    return name, id_medicament


def getJoursPrise(id_medicament):
    conn = sqlite3.connect('./database.db')
    cursor = conn.execute(
        "SELECT lundi,mardi,mercredi,jeudi,vendredi,samedi,dimanche FROM prise Where id_medicament=" + str(
            id_medicament))
    days = ""
    for row in cursor:
        days = row
    return days[0:7]


def changeJoursPrise(id_medicament, lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche):
    conn = sqlite3.connect('./database.db')
    conn.execute(
        "UPDATE prise SET lundi =" + str(lundi) + ",mardi=" + str(mardi) + ",mercredi=" + str(
            mercredi) + ",jeudi=" + str(jeudi) + ",vendredi=" + str(vendredi) + ",samedi=" + str(
            samedi) + ",dimanche=" + str(dimanche) + " where id_medicament =" + str(id_medicament))
    conn.commit()


def ajoutPrise(id_medicament, lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche):
    conn = sqlite3.connect('./database.db')
    conn.execute(
        "INSERT INTO prise(id_medicament,rappel,lundi,mardi,mercredi,jeudi,vendredi,samedi,dimanche) VALUES (" +
        str(id_medicament) + "," + str(0) + "," + str(lundi) + ", " + str(mardi) + ", " + str(
            mercredi) + ", " + str(
            jeudi) + "," + str(vendredi) + "," + str(samedi) + "," + str(dimanche) + " )")
    conn.commit()


def getNomsMedicamentsPasRemplis():
    conn = sqlite3.connect('./database.db')
    cursor = conn.execute(
        "SELECT medicaments.nom_court,cip,prise.id_medicament FROM medicaments,prise WHERE "
        "medicaments.id=prise.id_medicament AND rappel=0")
    liste = list()
    for row in cursor:
        liste.append(row[0])
    return liste


def getSiRempliOuNon(cip):
    conn = sqlite3.connect('./database.db')
    cursor = conn.execute(
        "SELECT prise.rappel from prise,medicaments where prise.id_medicament==medicaments.id and medicaments.cip='" + str(
            cip) + "'")
    rempli = 0
    code = 404
    for row in cursor:
        rempli = row[0]
        code = 200
    return rempli == 1, code


def suppression_prise(id_medicament):
    conn = sqlite3.connect('./database.db')
    conn.execute(
        "DELETE FROM prise where id_medicament="+str(id_medicament)+"")
    conn.commit()
