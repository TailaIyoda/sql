import sqlite3

#variables
DATABASE = "pokemon.db"
VALID_TYPES = [
    "normal", "fire", "water", "grass", "electric", "ice", "fighting", "poison",
    "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark",
    "steel", "fairy"
]
#functions
#function for printing all pokemons
def print_all_pokemon():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"SELECT * FROM pokemon;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('\033[33mdex number  pokemon name    type\n--------------------------------') #colour coded to yellow
    for pokemon in results:
        print(f"\033[31m{pokemon[0]:<11} \033[34m{pokemon[1]:<15} \033[32m{pokemon[2]:<10}\033[0m")    #inequality sign makes the output neat and colour coded

#function for printing all pokemons of a type
def print_all_type(poke_type_string):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"SELECT * FROM pokemon WHERE lower(pokemon_type) LIKE '%{poke_type_string.lower()}%';" #lower(pokemon_type) so inputs like "WaTeR" will work
    cursor.execute(sql)
    results = cursor.fetchall()
    print('\033[33mdex number  pokemon name    type\n--------------------------------')
    for pokemon in results:
        print(f"\033[31m{pokemon[0]:<11} \033[34m{pokemon[1]:<15} \033[32m{pokemon[2]:<10}\033[0m")  
    db.close()

#function for printing all pokemons of only one type
def print_only_type(poke_type_string):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"SELECT * FROM pokemon WHERE lower(pokemon_type) == '{poke_type_string.lower()}';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('\033[33mdex number  pokemon name    type\n--------------------------------')
    for pokemon in results:
        print(f"\033[31m{pokemon[0]:<11} \033[34m{pokemon[1]:<15} \033[32m{pokemon[2]:<10}\033[0m")  
    db.close()

#function for searching pokemon by name
def search_pokemon_name():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"SELECT * FROM pokemon WHERE lower(pokemon_name) LIKE '%{poke_type_string.lower()}%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('\033[33mdex number  pokemon name    type\n--------------------------------')
    for pokemon in results:
        print(f"\033[31m{pokemon[0]:<11} \033[34m{pokemon[1]:<15} \033[32m{pokemon[2]:<10}\033[0m")  
    db.close()

def search_pokemon_dex():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"SELECT * FROM pokemon WHERE pokemon_id = {pokedex_number};"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('\033[33mdex number  pokemon name    type\n--------------------------------')
    for pokemon in results:
        print(f"\033[31m{pokemon[0]:<11} \033[34m{pokemon[1]:<15} \033[32m{pokemon[2]:<10}\033[0m")  
    db.close()


#ask what the user wants to print

print('======== \033[38;5;208mPokemon Generation 1 Database \033[0m========')
print('\033[1m     _____           _____           _____')
print('\033[1m   =       =       =       =       =       =')
print('\033[1m =    ___    =   =    ___    =   =    ___    =')
print('\033[1m ====     ====   ====     ====   ====     ====')
print('\033[1m =    ---    =   =    ---    =   =    ---    =')
print('\033[1m   = _____ =       = _____ =       = _____ =')
while True:  #keeps asking until input is 6 (exit)
    first_input = input('\n\033[1;36mWhich pokemons do you want to print?\n\033[38;5;208m1.\033[0m Print all pokemons\n\033[38;5;208m2.\033[0m select pokemons by pokemon type \n\033[38;5;208m3.\033[0m select pokemons with only one type\n\033[38;5;208m4.\033[0m search by name \n\033[38;5;208m5.\033[0m search by pokedex number\n\033[38;5;208m6.\033[0m exit\n')


#code for when someone wants to print all pokemons
    if first_input == "1":
        print_all_pokemon()

# code for when someone wants to print pokemons of a type
    if first_input == "2":
        poke_type_string = input('Which type?\nnormal   fire      water   grass   electric    ice        fighting    poison   ground\nflying   psychic   bug     rock    ghost       dragon     dark        steel    fairy\nEnter the pokemon type\n')
        if poke_type_string.lower() in VALID_TYPES:
            print_all_type(poke_type_string)
        else:
            print("\033[1mThat is not a type.")

#code for when the user wants to print pokemons of only one type
    if first_input == "3":
        poke_type_string = input('normal   fire      water   grass   electric    ice        fighting    poison   ground\nflying   psychic   bug     rock    ghost       dragon     dark        steel    fairy\nEnter the pokemon type\n')
        if poke_type_string.lower() in VALID_TYPES:
            print_only_type(poke_type_string)
        else:
            print("\033[1mThat is not a type.")
    
    elif first_input == "4": # search pokemon by pokemon
        poke_type_string = input('Enter pokemon name:\n')
        search_pokemon_name()
        
    elif first_input == "5": #search pokemon by pokedex number
        poke_type_string = input('Enter pokedex number: ') 
        try:
            pokedex_number = int(poke_type_string)
            if 1 <= pokedex_number <= 151:
                search_pokemon_dex()
        except ValueError:
            print('\033[1menter number from 1-151')
        
        
    elif first_input == '6': #exit program
        break 

    else:
        print('\033[1mplease enter numbers 1-6')
