import json
vardss = input('ievadiet vardu: ')
uzvardss = input('ievadiet uzvardu: ')
vecumss = input('ievadiet vecumu: ')
tell = input('ievadiet telefona numuru: ')

vardnica = {
    'Vards':vardss,
    'Uzvards':uzvardss,
    'Vecums':vecumss,
    'Telefona Numurs':tell
}

def dati(vards,uzvards,vecums,tel):
    with open('ievaktieDati.json','a',encoding='utf-8') as outfile:
        
        json.dump(vardnica,outfile,indent=4,ensure_ascii=False)

dati(vardss,uzvardss,vecumss,tell)