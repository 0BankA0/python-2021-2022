import sqlite3
import datetime

db = sqlite3.connect('noliktava1.db')

db.execute("""CREATE TABLE IF NOT EXISTS noliktava1
    (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    produkcijas_veids TEXT NOT NULL,
    daudzums_kg INT NOT NULL,
    datums_kad_tika_atvesta INT NOT NULL
    )""")



def datuievade():
    while True:
        produkcijas_veids = input('Kas tiek ievests noliktava: ')
        if produkcijas_veids.isdigit() == False:
            if produkcijas_veids.strip() == '':                
                continue
            else:
                break
        else:
            continue
        

    while True:
        daudzums_kg = input('ievadi svaru(kg) ')
        if daudzums_kg.isdigit():
            break
        else:
            continue

    while True:
        datums_kad_tika_atvesta = input('Ievadiet atvešanas datumu(DD/MM/YYYY): ')
        break
    
    db.execute("""INSERT INTO noliktava1
                (produkcijas_veids,daudzums_kg,datums_kad_tika_atvesta)
                VALUES (:produkcijas_veids,:daudzums_kg,:datums_kad_tika_atvesta)
    """,{'produkcijas_veids':produkcijas_veids,'daudzums_kg':daudzums_kg,'datums_kad_tika_atvesta':datums_kad_tika_atvesta})

    db.commit()
datuievade()