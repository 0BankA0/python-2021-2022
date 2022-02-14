import csv
def csv_1_2(pirmaiscsv, otraiscsv):
    with open(pirmaiscsv, 'r',encoding="utf-8") as fails:
        lasit_csv = csv.reader(fails)
        saturs= []
        for rinda in lasit_csv:
            saturs.append(rinda)
    
    with open(otraiscsv, 'r',encoding="utf-8") as fails:
        lasit_csv = csv.reader(fails)
        saturs_otrajam= []
        for rinda in lasit_csv:
            saturs_otrajam.append(rinda)
    
    if len(saturs) == len(saturs_otrajam):
        with open('divikopa.csv', 'w',encoding="utf-8",newline='') as fails:
            csvwrite= csv.writer(fails)
            csvwrite.writerows(saturs)
            csvwrite.writerows(saturs_otrajam)

    unicalie = []

    for unik in saturs:
        if unik not in saturs_otrajam:
            unicalie.append(unik)
    print(unicalie)
    
    vienadi = []

    for vien in saturs:
        if vien in saturs_otrajam:
            vienadi.append(vien)
    print(vienadi)

csv_1_2("pirmais.csv","otrais.csv")
