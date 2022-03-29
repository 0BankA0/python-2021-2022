import sqlite3
import datetimea

start=datetimea.now()

db = sqlite3.connect("titanicDB.db")

#tabulu_nosaukumi = db.execute("SELECT name FROM sqlite_shema WHERE type = 'table'")
#
#rezultats = tabulu_nosaukumi.fetchall()
#print(rezultats)

