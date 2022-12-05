import pandas as pd
import xlrd

document = xlrd.open_workbook('../ressources/ressources.xlsx')
feuille_1 = document.sheet_by_index(0)
buffer = ""
f = open("result/test.txt", "a")
f.write("INSERT INTO medicaments(id,cip,cip_ucd,nom_court)\nVALUES\n")
for i in range(1, feuille_1.nrows):
    buffer += "("
    buffer += str(i) + ","
    for j in range(0, feuille_1.ncols):

        buffer += "\"" + feuille_1.cell(rowx=i, colx=j).value + "\""
        if j < 2:
            buffer += ","
    buffer += "),\n"
f.write(buffer)
