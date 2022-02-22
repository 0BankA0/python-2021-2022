import json
vards = input('ievadiet vardu: ')
uzvards = input('ievadiet uzvardu: ')
vecums = input('ievadiet vecumu: ')
tell = input('ievadiet telefona numuru: ')

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

