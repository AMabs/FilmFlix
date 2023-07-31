from connectDB import *
from time import sleep

def readFilms():
    cursor.execute("SELECT * FROM tblFilms")
    row = cursor.fetchall()
    sleep(1)
    for record in row:
        print(record)

if __name__ =="__main__":
    readFilms()