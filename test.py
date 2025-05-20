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
    print('dex number  pokemon name    type')
    for pokemon in results:
        print(f"{pokemon[0]:<5} {pokemon[1]:<12} {pokemon[2]:<10}")
    db.close()

def print_all_water():
    db = sqlite3.connect("pokemon.db")
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type LIKE '%Water%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number  pokemon name    type')
    for pokemon in results:
        print(f"{pokemon[0]:<5} {pokemon[1]:<12} {pokemon[2]:<10}")
    db.close()

def print_only_water():
    db = sqlite3.connect("pokemon.db")
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type = 'Water';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number  pokemon name    type')
    for pokemon in results:
        print(f"{pokemon[0]:<5} {pokemon[1]:<12} {pokemon[2]:<10}")
    db.close()

#What would you like to do.\n1. Print all pokemon\n2. Print all water type pokemons            3. Print water ONLY pokemons\n
#maincode
while True:
    print('To print all pokemons, write "all"\n')
    print('To print pokemons that are the same types, write "Print...."\nExample: "Print water" or "Print fire"\n')
    print('If you want to print pokemons that are only one specific type, enter "Print only....."\nExample: "Print only water" or "Print only fire"\n')
    user_input = input('If you want to finish type "finish"')
    if user_input == "all":
        print_all_pokemon()
    elif user_input == "Print water":
        print_all_water()
    elif user_input == "Print only water":
        print_only_water()
    elif user_input == "finish":
        break
