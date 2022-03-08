from hmac import trans_36
import re
import sqlite3

db = sqlite3.connect("test.db")
#Tabulas izveidošana
#db.execute("""CREATE TABLE IF NOT EXISTS edienkarte
#    (id        INT       PRIMARY KEY      NOT NULL,
#    nosaukums  TEXT      NOT NULL,
#    cena       REAL      NOT NULL,
#    alergeni   CHAR(50)
#    
#    )""")

#Datu pievineošana
#db.execute("""INSERT INTO edienkarte
#            (id,nosaukums,cena,alergeni)
#            VALUES (5, 'Zirņu zupa', 1.8, 'glutēns')
#            
        
#""")

#db.commit()

#dati = db.execute("SELECT* FROM edienkarte WHERE cena > 0.5")
#rezultats = dati.fetchall()
#
#print(rezultats)

#db.execute("""CREATE TABLE IF NOT EXISTS sastavdalas
#    (id        INTEGER       PRIMARY KEY AUTOINCREMENT     NOT NULL,
#    pirma   CHAR(50)      NOT NULL,
#    otra    CHAR(50),
#    tresa   CHAR(50)
#    
#    )""")

#pirma = input("pirma sastavdaļā: ")
#otra = input("otra sastavdaļā: ")
#tresa = input("trsa sastavdaļā: ")

#db.execute("""INSERT INTO sastavdalas
#            (pirma, otra, tresa)
#            VALUES (:pirma, :otra, :tresa)
            
#""",{'pirma':pirma,'otra':otra, 'tresa':tresa})
#db.commit()

dati = db.execute("SELECT * FROM edienkarte")
for rinda in dati:
    print("ID: ", rinda[0])
    print("cena:", rinda[2])
    print("Alergēni:", rinda[3], "\n")
db.close()