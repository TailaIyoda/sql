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
    first_input = input('Would you like to input,\n1. all\n2.pokemons of type \n3. pokemons of only one type\nfinish\nChoose from 1, 2, 3 or 4\n')


#code for when someone wants to print all pokemons
    if first_input == "1":
        print_all_pokemon()

# code for when someone wants to print pokemons of a type
    if first_input == "2":
        poke_type_string = input('Which type?\nnormal\nfire\nwater\ngrass\nelectric\nice\nfighting\npoison\nground\nflying\npsychic\nbug\nrock\nghost\ndragon\ndark\nsteel\nfairy\nEnter the pokemon type\n')
        if poke_type_string in VALID_TYPES:
            print_all_type(poke_type_string)
        else:
            print("That is not a type.")

#code for when the user wants to print pokemons of only one type
    if first_input == "3":
        poke_type_string = input('Which type?\nnormal\nfire\nwater\ngrass\nelectric\nice\nfighting\npoison\nground\nflying\npsychic\nbug\nrock\nghost\ndragon\ndark\nsteel\nfairy\nEnter the pokemon type\n')
        if poke_type_string in VALID_TYPES:
            print_only_type(poke_type_string)
        else:
            print("That is not a type.")
    
    if first_input == "4"
        break
    #Solution for non pokemon type inputs
    else:
        print("Invalid input. Try again.")
