import readFilms, addFilms, updateFilms, deleteFilms, searchReport

def read_file():
    try:
        with open("FilmflixDB/menuOptions.txt") as fileRead:
            fr = fileRead.read()
        return fr
    except FileNotFoundError as nf:
        print(f"Check {nf}")
        print(f"File not found: {nf}")
    raise  # Re-raise the exception for proper handling
  

# create the menu function 
def tblFilms_menu():
    option = 0 # initialise theoption variable with an integere value
    optionsList = ["1","2","3","4","5","6"]

    # assign the  read_file() function to the menuChoices variable 
    menuChoices =  read_file()

    # create a while loop to repeat the code within the body of while condition
    while option not in optionsList:
        print(menuChoices) # call/invoke read_file() function to the menuChoices variable 

        # re-assign the valeu of the option variable with the input function 
        option = input("Enter an option from the Menu choice above: ")

        # check if the input from the option variable match any of the options 
        # in the optionsList(["1","2","3","4","5","6"]) 
        if option not in optionsList:
            # if the condition above is true execute the code below
            print(f"{option} is not a valid choice! ")
        while option not in optionsList:
            print(menuChoices)
            option = input("Enter an option from the Menu choice above: ")
        if not option.isdigit() or option not in optionsList:
            print("Invalid input. Please enter a valid option.")
    return option


mainProgram = True # Boolean variabe to toggle True/False

while mainProgram: #While True
    # assign the tblFilms_menu() function to the mainMenu variable 
    mainMenu = tblFilms_menu()
    
    # use match case 
    match mainMenu:
        case "1": # if case value equals/matches the string value 1 then 
            readFilms.read_tblFilms() # call the read_tblFilms()  from the readFilms.py file imported at the top
        case "2":
            addFilms.insert_tblFilms()
        case "3":
            updateFilms.update_tblFilms()
        case "4":
            deleteFilms.delete_tblFilms()
        case "5":
            searchReport.search()
        case _:
            #reassign the value of mainprogram to False
            mainProgram = False
input("Press Enter key to exit the program: ")


    


 
