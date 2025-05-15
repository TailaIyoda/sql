import sqlite3

db = sqlite3.connect("pokemon.db")
surcor = db.cursor()
sql = "select * from pokemon"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()