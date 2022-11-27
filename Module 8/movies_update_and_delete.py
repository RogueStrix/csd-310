import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "port": "3006",
    "database": "movies",
    "raise_on_warnings": True
}


def show_films(cursor, title):
    #executes an inner join on all tables,
    #   iterate over the dataset and output the results to the terminal window

    #inner join query
    cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    #get the results from the cursor object
    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    #iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    #Shows the default film selections
    show_films(cursor, "DISPLAYING FILMS")

    #Adds Back to the Future to the Database Table Film
    cursor.execute("INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)"
                   "VALUES('Back to the Future', '1985', '116', 'Robert Zemeckis', "
                   "(SELECT studio_id FROM studio WHERE studio_name = 'Universal Pictures'),"
                   "(SELECT genre_id FROM genre WHERE genre_name = 'SciFi') );")

    #Shows the film selections after adding a movie
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    #Updates the genre of Alien to Horror
    cursor.execute("UPDATE film SET genre_id = 1 WHERE film_id = 2")

    #Shows the film selections after changing the genre of Alien to horror
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")

    #Deletes Gladiator from the Database
    cursor.execute("DELETE FROM film WHERE film_id = 1")

    #Shows the film selections after deleting Gladiator
    show_films(cursor, "DISPLAYING FILMS AFTER DELETING GLADIATOR")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

finally:
    db.close()
