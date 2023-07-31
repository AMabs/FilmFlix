from read import readFilms
from add import addFilm
from update import updateFilms
from delete import deleteFilm
from filter import filterFilms

def menuOptions():
    options = 0
    while options not in ["1","2","3","4","5"]:
        print("Main menu options\nEnter: \n1 - To add a film.\n2 - To delete a film.\n3 - To amend a film.\n4 - To print all films.\n5 - To filter films.\n6 - To Exit.")
        options = input("\nEnter any one of the options above: ")
        if options not in ["1","2","3","4","5"]:
            print(f"{options} is not a valid choice")
    return options

mainProgram = True
while mainProgram:
    mainMenu = menuOptions() 
    if mainMenu == "1":
        addFilm() 
    elif mainMenu == "2":
        deleteFilm()
    elif mainMenu == "3":
        updateFilms()
    elif mainMenu == "4":
        readFilms()
    elif mainMenu == "5":
        filterFilms()
    else:
        mainProgram = False
input("Press enter to Exit")