import csv
from fileinput import close

file = open("csv_meg.csv")

print(type(file))

lasit_csv = csv.reader(file)

print(lasit_csv)

header = []
header = next(lasit_csv)
print(header)

saturs = []
for rinda in lasit_csv:
    saturs.append(rinda)

print(saturs)
print(saturs)

file.close()

kolonnuNosaukims = [['vares'], ['1.atzime'], ['2.atzime']]
dati = [['peteris', 6,8], ['Janis', 2, 7], ['gatis', 2, 2 ]]

with open('skolenu_dati.csv', 'w',encoding="utf-8",newline='') as fails:
    csvwrite= csv.writer(fails)
    csvwrite.writerows(kolonnuNosaukims)
    csvwrite.writerows(dati)
with open('skolenu_dati.csv', 'r', encoding="utf-8") as fails:
    lasit_csv = csv.reader(fails)
    saturs = []
    for rinda in lasit_csv:
        saturs.append(rinda)

    print(len(saturs))

    print(saturs[0])

    for s in range(3):
        print(saturs[s])
def izvadit_funkc(datnessnosaukums, elemnumurs):
    with open(datnessnosaukums, 'r', encoding="utf-8") as fails:
        lasit_csv = csv.reader(fails)
        saturs = []
        for rinda in lasit_csv:
            saturs.append(rinda)
        print(saturs[elemnumurs])
izvadit_funkc('skolenu_dati.csv',1)
