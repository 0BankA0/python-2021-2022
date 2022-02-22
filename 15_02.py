import json

while True:
        tell = input("Ievadi savu telefona numuru: ")
        if len(tell) <8:
            continue
        else:
             break



while True:
    vecums = input("Ievadi savu vecumu: ")
    if vecums.isdigit() == True:
        break
    else:
        continue



while True:
    vards = input("Ievadi savu vardu: ")
    if vards.strip() == "":
        print("ievadi vardu atkartoti: ")
        continue
    else:
        break

while True:
    uzvards = input("Ievadi savu vardu: ")
    if uzvards.strip() == "":
        print("ievadi vardu atkartoti: ")
        continue
    else:
        break

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

