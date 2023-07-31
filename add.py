from connectDB import *
from time import sleep
from read import readFilms

def addFilm():
    films = []

    filmTitle = input("Enter film title: ")
    yearReleased = int(input("Enter film year of release: "))
    rating = input("Enter film rating: ")
    duration = int(input("Enter film duration: "))
    genre = input("Enter film genre: ")

    films.append(filmTitle)
    films.append(yearReleased)
    films.append(rating)
    films.append(duration)
    films.append(genre)

    cursor.execute("INSERT INTO tblFilms VALUES(NULL,?,?,?,?,?)", films)
    conn.commit()

    print(f"{filmTitle} added to records")

    sleep(1)
    readFilms()

if __name__ =="__main__":
    addFilm()