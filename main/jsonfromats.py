import json
from xml.dom.minidom import Identified

#vārdnīca

vardnica = {
    "vards":"Janis",
    "izglitiba":"Vidēja",
    "Vecums": 25
}

#parvedot pthn uz json
a = json.dumps(vardnica)

print(a)

#parvedot Json uz pthon
b= json.loads(a)

print(json.dumps(["kivi", "citrons"]))

#dict - Object
#list - Array
#tuple - Array
#str - String
#int - Number
#float - Number
#True - true
#False - false
#None - null

py_data = {
    "Vards":"Boris",
    "Vecums":30,
    "Dzivs":True,
    "NeDzivs":False,
    "Berni":("Gatis", "Anna"),
    "Dzivnieki":None,
    "Masinas":[
        {"Modelis":"BMW M8", "Gads":2020},
        {"Modelis":"Audi RS6 C8", "Gads":2020}
    ]
}

print(json.dumps(py_data, indent=4, separators=(".", "=")))

with open("pirmais_json.json", "w") as fails:
    json.dump(py_data,fails, indent=4, ensure_ascii=False)

with open("pirmais_json.json", "r") as fails:
    json_dati = json.load(fails)

    #vardnicas garums
    print(len(json_dati))

    #visas ataslēgas
    print(json_dati.keys())

    #visas vērtibas
    print(json_dati.values())

    #Parbaudi, vai dota atslēga it vardnīca in izvadit ts vērtibu

    atsl1 = "Vecunms"
    atsl_par = ""

    for atslega in json_dati.keys():
        if atslega == atsl1:
            ista_atslega = atslega
            print(json_dati[atslega])
    if atsl1 != atsl_par:
        print(f"Izskatas, ka {atsl1} nav atrasta")


#Nodefinet funkciju, kura kā argumentus izmatos
# datnes nosaukumu un atslēgas nosaukumu
# jaizvada atslegas vērtiba