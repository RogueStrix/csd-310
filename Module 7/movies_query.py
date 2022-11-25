import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "ThisIsForClass01!",
    "host": "127.0.0.1",
    "port": "3006",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    #Selects and shows all studio ids and studio names
    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()
    print("-- DISPLAYING Studio RECORDS --")
    for studio in studios:
        print ("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

    #Selects and shows all genre ids and genre names
    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()
    print("-- DISPLAYING Genre RECORDS --")
    for genre in genres:
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

    # Selects film name and runtime as long as runtim is more than 120 minutes and displays them
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    films = cursor.fetchall()
    print("-- DISPLAYING Short Film RECORDS --")
    for film in films:
        print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))

    cursor.execute("select film_name, film_director from film order by film_director;")
    films = cursor.fetchall()
    print("-- DISPLAYING Director RECORDS in Order --")
    for film in films:
        print("Film Name: {}\nDirector: {}\n".format(film[0], film[1]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
