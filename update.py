from connectDB import *
from time import sleep
from read import readFilms

def updateFilms():
    idField = input("Enter the ID for the record to be updated: ")
    fieldName = input("Which field would you like to update (Title/Year of release/Rating/Duration/Genre)? ").title()
    newFieldValue = input(f"Enter the field's new value for {fieldName}: ")
    print(f"The new field value is {newFieldValue}")

    newFieldValue = "'" + newFieldValue + "'"
    print(f"Amended new field value is {newFieldValue}")
    
    cursor.execute(f"UPDATE tblFilms SET {fieldName} = {newFieldValue} WHERE filmID = {idField}")
    conn.commit()

    print(f"Record {idField} successfully updated")

    sleep(1)
    readFilms()

if __name__ =="__main__":
    updateFilms()