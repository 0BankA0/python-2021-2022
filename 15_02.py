import json

while True:
    vardss = input('ievadiet vardu: ')
    if vardss.isdigit() == False:
        if vardss.strip() == '':
            print('ievadiet vardu atkartoti')
            continue
        else:
            break
    else:
        print('ievadiet vardu atkartoti')
        continue

        

while True:
    uzvardss = input('ievadiet uzvardu: ')
    if uzvardss.isdigit() == False:
        if uzvardss.strip() == '':
            print('ievadiet uzvardu atkartoti')
            continue
        else:
            break
    else:
        print('ievadiet uzvardu atkartoti')
        continue


while True:
    vecumss = input('ievadiet vecumu: ')
    if vecumss.isdigit():
        break
    else:
        print('ievadiet vecumu atkartoti')
        continue

while True:
    tell = input('ievadiet telefona numuru: ')
    if tell.isdigit():
        if len(tell) == 8:
            break
    else:
        print('ievadiet telefona numuru atkartoti')
        continue

ievad_dati = {
    "Uzvārds":uzvards,
    "Vecums":vecums,
    "Telefona numurs":tell
}

with open("ievaktieDati.json","r", encoding="utf-8") as fails:
    json_data = json.load(fails)

    ir_saraksta =False
    for key in json_data.keys():
        if key == vards:
            break
        if key != vards:
            ir_saraksta = True

    if ir_saraksta == False:
        print("Vārds ir sarakstā")
    else:
        json_data[vards]=ievad_dati

with open("ievaktieDati.json","w", encoding="utf-8") as fails:
    json.dump(json_data,fails, indent = 4, ensure_ascii=False)

