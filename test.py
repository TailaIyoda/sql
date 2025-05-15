import sqlite3

DATABASE = 'pokemon.db'

def print_all_pokemon():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM pokemon;"
        cursor.execute(sql)
        results = cursor.fetchall()

        for pokemon in results:
            print(f'pokedex: {pokemon[0]} name: {pokemon[1]} type: {pokemon[2]}')

if __name__ == "__main__":
    print_all_pokemon()