from connectDB import *
from time import sleep
from read import readFilms

def deleteFilm():
    idField = input("Enter the filmID for the record to be deleted: ")
    
    cursor.execute(f"DELETE FROM tblFilms WHERE filmID = {idField}")
    conn.commit()

    print(f"Record {idField} successfully deleted")

    sleep(1)
    readFilms()

if __name__ =="__main__":
    deleteFilm()