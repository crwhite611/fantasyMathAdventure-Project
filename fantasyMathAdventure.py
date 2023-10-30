# This is an awesome python project written and designed by LJ, Nathan, and Callie

from collections import namedtuple
import time # Allows use of sleep function; makes the program look cooler

# \/ Declare question lists here \/

easyQuestions = []
mediumQuestions = []
hardQuestions = []

playerCharacter = namedtuple('playerCharacter',['name','race', 'health', 'critTime']) # Creates "mould" for character object; allows us to map characteristics to character name
playerStartInput = input("Welcome to Fantasy Math Adventure!\n\nTo play, type: \'Go\' \nTo quit, type: \'q\'\n") # Gotta start off the while loop ;) "start menu"

while playerStartInput != 'q': # While loop keeps game going til player "quits"

# Charcter Selection Walkthrough

    print("\nThis is the Character Selecter. Each character has unique abilities, ranging from different healths, to crit times, to special powers.\n")
    time.sleep(6) # From imported 'time' module; counts specified seconds before executing next line of code; makes the program look cooler 
    print("A creature's health determinds how much damage it can take, while its crit time is how long you can take to answer a question correctly and still deal critical damage.\n")
    time.sleep(6)
    print("Some creatures also have special abilities to give you some extra help along the way.\n")
    time.sleep(4)
    print("To select your character, type the number by your character's name:\n")

    print("1. Name: Rush\n   Race: Elf\n   Health: 8\n   Crit time: 8 Seconds\n   Special Ability: Once you have a two question streak, you will regain two life per correct answer\n")
    print("2. Name: Samson\n   Race: Hobbit\n   Health: 10\n   Crit time: 7 Seconds\n   Special Ability: Upon a wrong answer, you get one extra chance to answer again before you take damage\n")
    print("3. Name: Rog\n   Race: Orc\n   Health: 12\n   Crit time: 6 Seconds\n   Special Ability: Once you have a two question streak, your crit time becomes unlimited\n")

# \/ Creates objects for each character \/ 

    rush = playerCharacter('Rush','Elf', '8','8')
    samson = playerCharacter('Samson','Hobbit', '10','7')
    rog = playerCharacter('Rog','Orc','12','6')

# \/ Take input for character selection \/

    characterSelection = input("")

# \/ Matches variable "character" to whichever one was selected \/

    match characterSelection:
        case '1':
            character = rush
            
        case '2':
            character = samson
           
        case '3':
            character = rog

    print(f'Awesome! You chose {character.name}!')    

