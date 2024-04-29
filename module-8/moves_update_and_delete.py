import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "AnnaOfArendelle1!2",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

def show_films(cursor, title ):
    cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")
    films = cursor.fetchall()
    print("\n -- {} --".format(title))
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

try:
    db = mysql.connector.connect(**config)
    print ("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    cursor = db.cursor()
    show_films(cursor, "DISPLAYING FILMS")
    input("\n\n Press any key to continue...")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERRROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)
finally:
    db.close()