from connectDB import *
from time import sleep 
import datetime
from read import readFilms

def filterGenre():
    genreDict = {"1": "Action", "2": "Animation", "3": "Crime", "4": "Comedy", "5": "Fantasy", "6": "Fighting"}
    filterOptions = 0
    while filterOptions not in ["1","2","3","4","5","6"]:
        print("Filter by the following genres:\n1 - Action\n2 - Animation\n3 - Crime\n4 - Comedy\n5 - Fantasy\n6 - Fighting")
        filterOptions = input("Which genre would you like to filter by: ")
        print(filterOptions)
        if filterOptions not in ["1","2","3","4","5","6"]:
            print("This is not a part of the available filter options") 
    #MySQL syntax: SELECT * FROM <table> WHERE <condition>;
    cursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{genreDict.get(filterOptions)}'")
    row = cursor.fetchall()
    sleep(1)
    for record in row:
        print(record)

def filterYear():
    yearR = input("Enter year of release: ")
    curDT = datetime.datetime.now()
    curY = curDT.strftime("%Y")
    if yearR <= curY:
        cursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = {yearR}")
        row = cursor.fetchall()
        sleep(1)
        for record in row:
            print(record)
    else:
        print(f"The year entered is invalid!\nThe year cannot be greater than the year {curY}.")

def filterRating():
    ratingDict = {"1": "PG", "2": "G", "3": "R"}
    filterOptions = 0
    while filterOptions not in ["1","2","3"]:
        print("Filter by the following ratings:\n1 - PG\n2 - G\n3 - R")
        filterOptions = input("Which rating would you like to filter by: ")
        print(filterOptions)
        if filterOptions not in ["1","2","3"]:
            print("This is not a part of the available filter options")
    cursor.execute(f"SELECT * FROM tblFilms WHERE rating = '{ratingDict.get(filterOptions)}'")
    row = cursor.fetchall()
    sleep(1)
    for record in row:
        print(record)

def filterFilms():
    options = 0
    while options not in ["1","2","3","4","5"]:
        print("Filter menu options:\nEnter: \n1 - To print details of all films.\n2 - To filter films based on genre.\n3 - To filter films based on year.\n4 - To filter films based on rating.\n5 - To return to main menu.")
        options = input("\nEnter any one of the options above: ")
        if options not in ["1","2","3","4","5"]:
            print(f"{options} is not a valid choice")
        elif options == "1":
            readFilms()
        elif options == "2":
            filterGenre()
        elif options == "3":
            filterYear()
        elif options == "4":
            filterRating()
        elif options == "5":
            return options
