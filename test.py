import sqlite3

#variable
DATABASE = "pokemon.db"

#function
def print_all_bug():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type LIKE '%Bug%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number  pokemon name    type')
    for pokemon in results:
        print(f"{pokemon[0]:<5} {pokemon[1]:<12} {pokemon[2]:<10}")
    db.close()

def print_all_dark():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type LIKE '%Dark%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number  pokemon name    type')
    for pokemon in results:
        print(f"{pokemon[0]:<5} {pokemon[1]:<12} {pokemon[2]:<10}")
    db.close()

def print_all_dragon():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type LIKE '%Dragon%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number  pokemon name    type')
    for pokemon in results:
        print(f"{pokemon[0]:<5} {pokemon[1]:<12} {pokemon[2]:<10}")
    db.close()

def print_all_electric():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type LIKE '%Electric%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number  pokemon name    type')
    for pokemon in results:
        print(f"{pokemon[0]:<5} {pokemon[1]:<12} {pokemon[2]:<10}")
    db.close()

def print_all_fairy():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type LIKE '%Fairy%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number  pokemon name    type')
    for pokemon in results:
        print(f"{pokemon[0]:<5} {pokemon[1]:<12} {pokemon[2]:<10}")
    db.close()

def print_all_fighting():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type LIKE '%Fighting%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number  pokemon name    type')
    for pokemon in results:
        print(f"{pokemon[0]:<5} {pokemon[1]:<12} {pokemon[2]:<10}")
    db.close()

def print_all_fire():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type LIKE '%Fire%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number  pokemon name    type')
    for pokemon in results:
        print(f"{pokemon[0]:<5} {pokemon[1]:<12} {pokemon[2]:<10}")
    db.close()

def print_all_flying():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type LIKE '%Flying%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number  pokemon name    type')
    for pokemon in results:
        print(f"{pokemon[0]:<5} {pokemon[1]:<12} {pokemon[2]:<10}")
    db.close()

def print_all_ghost():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type LIKE '%Ghost%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number  pokemon name    type')
    for pokemon in results:
        print(f"{pokemon[0]:<5} {pokemon[1]:<12} {pokemon[2]:<10}")
    db.close()

def print_all_grass():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type LIKE '%Grass%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number  pokemon name    type')
    for pokemon in results:
        print(f"{pokemon[0]:<5} {pokemon[1]:<12} {pokemon[2]:<10}")
    db.close()

def print_all_ground():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type LIKE '%Ground%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number  pokemon name    type')
    for pokemon in results:
        print(f"{pokemon[0]:<5} {pokemon[1]:<12} {pokemon[2]:<10}")
    db.close()

def print_all_ice():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type LIKE '%Ice%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number  pokemon name    type')
    for pokemon in results:
        print(f"{pokemon[0]:<5} {pokemon[1]:<12} {pokemon[2]:<10}")
    db.close()

def print_all_normal():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type LIKE '%Normal%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number  pokemon name    type')
    for pokemon in results:
        print(f"{pokemon[0]:<5} {pokemon[1]:<12} {pokemon[2]:<10}")
    db.close()

def print_all_poison():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type LIKE '%Poison%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number  pokemon name    type')
    for pokemon in results:
        print(f"{pokemon[0]:<5} {pokemon[1]:<12} {pokemon[2]:<10}")
    db.close()

def print_all_psychic():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type LIKE '%Psychic%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number  pokemon name    type')
    for pokemon in results:
        print(f"{pokemon[0]:<5} {pokemon[1]:<12} {pokemon[2]:<10}")
    db.close()

def print_all_rock():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type LIKE '%Rock%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number  pokemon name    type')
    for pokemon in results:
        print(f"{pokemon[0]:<5} {pokemon[1]:<12} {pokemon[2]:<10}")
    db.close()

def print_all_steel():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type LIKE '%Steel%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number  pokemon name    type')
    for pokemon in results:
        print(f"{pokemon[0]:<5} {pokemon[1]:<12} {pokemon[2]:<10}")
    db.close()

def print_all_water():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type LIKE '%Water%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number  pokemon name    type')
    for pokemon in results:
        print(f"{pokemon[0]:<5} {pokemon[1]:<12} {pokemon[2]:<10}")
    db.close()
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM pokemon WHERE pokemon_type = 'Flying';"
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
    print('To print pokemons that are the same types, write "print...."\nExample: "rint water" or "print fire"\n')
    print('If you want to print pokemons that are only one specific type, enter "only....."\nExample: "only water" or "only fire"\n')
    user_input = input('If you want to finish type "finish"\n')
    if user_input == "all":
        print_all_pokemon()
    elif "print" in user_input:
        if "bug" in user_input:
            print_all_bug()
        elif "dark" in user_input:
            print_all_dark()
        elif "dragon" in user_input:
            print_all_dragon()
        elif "electric" in user_input:
            print_all_electric()
        elif "fairy" in user_input:
            print_all_fairy()
        elif "fighting" in user_input:
            print_all_fighting()
        elif "fire" in user_input:
            print_all_fire()
        elif "flying" in user_input:
            print_all_flying()
        elif "ghost" in user_input:
            print_all_ghost()
        elif "grass" in user_input:
            print_all_grass()
        elif "ground" in user_input:
            print_all_ground()
        elif "ice" in user_input:
            print_all_ice()
        elif "normal" in user_input:
            print_all_normal()
        elif "poison" in user_input:
            print_all_poison()
        elif "psychic" in user_input:
            print_all_psychic()
        elif "rock" in user_input:
            print_all_rock()
        elif "steel" in user_input:
            print_all_steel()
        elif "water" in user_input:
            print_all_water()
    elif "only" in user_input:
        if "bug" in user_input:
            print_all_bug()
        elif "dark" in user_input:
            print_all_dark()
        elif "dragon" in user_input:
            print_all_dragon()
        elif "electric" in user_input:
            print_all_electric()
        elif "fairy" in user_input:
            print_all_fairy()
        elif "fighting" in user_input:
            print_all_fighting()
        elif "fire" in user_input:
            print_all_fire()
        elif "flying" in user_input:
            print_all_flying()
        elif "ghost" in user_input:
            print_all_ghost()
        elif "grass" in user_input:
            print_all_grass()
        elif "ground" in user_input:
            print_all_ground()
        elif "ice" in user_input:
            print_all_ice()
        elif "normal" in user_input:
            print_all_normal()
        elif "poison" in user_input:
            print_all_poison()
        elif "psychic" in user_input:
            print_all_psychic()
        elif "rock" in user_input:
            print_all_rock()
        elif "steel" in user_input:
            print_all_steel()
        elif "water" in user_input:
            print_all_water()
    elif user_input == "finish":
        break
