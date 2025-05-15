import sqlite3

#variable
DATABASE = "pokemon.db"


#function
def print_all_pokemon():
    db = sqlite3.connect("pokemon.db")
    cursor = db.cursor()
    sql = "select * from pokemon"
    cursor.execute(sql)
    results = cursor.fetchall()
    for pokemon in results:
        print(f"pokedex: {pokemon[0]}, pokemon: {pokemon[1]}, type: {pokemon[2]}")
    db.close()



#maincode
print_all_pokemon()