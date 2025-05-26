import sqlite3

#variables
DATABASE = "pokemon.db"
VALID_TYPES = [
    "normal", "fire", "water", "grass", "electric", "ice", "fighting", "poison",
    "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark",
    "steel", "fairy"
]
#functions
#functino for printing all pokemons
def print_all_pokemon():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"SELECT * FROM pokemon;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number | pokemon name  |  type')
    for pokemon in results:
        print(f"{pokemon[0]:<12} {pokemon[1]:<16} {pokemon[2]:<11}")
    db.close()

#function for printing all pokemons of a type
def print_all_type(poke_type_string):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"SELECT * FROM pokemon WHERE lower(pokemon_type) LIKE '%{poke_type_string}%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number | pokemon name  |  type')
    for pokemon in results:
        print(f"{pokemon[0]:<12} {pokemon[1]:<16} {pokemon[2]:<11}")
    db.close()

#function for printing all pokemons of only one type
def print_only_type(poke_type_string):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"SELECT * FROM pokemon WHERE lower(pokemon_type) == '{poke_type_string}';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('dex number  pokemon name    type')
    for pokemon in results:
        print(f"{pokemon[0]:<11} {pokemon[1]:<15} {pokemon[2]:<10}")
    db.close()


#ask what the user wants to print
while True:
    print('To print all pokemons, write "all"\n')
    print('To print pokemons that are the same types, write "print...."\nExample: "rint water" or "print fire"\n')
    print('If you want to print pokemons that are only one specific type, enter "only....."\nExample: "only water" or "only fire"\n')
    user_input = input('If you want to finish type "finish"\n')

#code for when someone wants to print all pokemons
    if user_input == "all":
        print_all_pokemon()

# code for when someone wants to print pokemons of a type
    elif user_input.startswith("print "):
        words = user_input.split()
        if len(words) >= 2:
            poke_type_string = words[1]
            if poke_type_string in VALID_TYPES:
                print_all_type(poke_type_string)
            else:
                print("That is not a type.")

#code for when the user wants to print pokemons of only one type
    elif user_input.startswith("only "):
        words = user_input.split()
        if len(words) >= 2:
            poke_type_string = words[1]
            if poke_type_string in VALID_TYPES:
                print_only_type(poke_type_string)
            else:
                print("That is not a type.")  
    elif user_input == "finish":
        break
    
    #Solution for non pokemon type inputs
    else:
        print("Invalid input. Try again.")
