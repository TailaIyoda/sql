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
    print('dex number     pokemon name          type')
    for pokemon in results:
        print(f"pokedex: {pokemon[0]:<5} pokemon: {pokemon[1]:<12} type: {pokemon[2]:<10}")
    db.close()

def print_all_water():
    db = sqlite3.connect("pokemon.db")
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type LIKE '%Water%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number     pokemon name          type')
    for pokemon in results:
        print(f"pokedex: {pokemon[0]:<5} pokemon: {pokemon[1]:<12} type: {pokemon[2]:<10}")
    db.close()

def print_only_water():
    db = sqlite3.connect("pokemon.db")
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type = 'Water';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number     pokemon name          type')
    for pokemon in results:
        print(f"pokedex: {pokemon[0]:<5} pokemon: {pokemon[1]:<12} type: {pokemon[2]:<10}")
    db.close()

#What would you like to do.\n1. Print all pokemon\n2. Print all water type pokemons            3. Print water ONLY pokemons\n
#maincode
while True:
    user_input = input('To print all pokemons, write "all"\nTo print pokemons that are the same types, write "Print...."\nExample: "Print water" or "Print fire"\n')
    if user_input == "all":
        print_all_pokemon()
    elif user_input =="Print water":
        print_all_water()
    elif user_input == "Print only water":
        print_only_water()
    elif user_input == "break":
        break
