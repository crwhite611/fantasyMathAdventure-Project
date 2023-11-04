# This is an awesome python project written and designed by LJ, Nathan, and Callie

from collections import namedtuple
import time # Allows use of sleep function; makes the program look cooler
import random
import math

# \/ Declare question dictionaries here; problem mapped to answer \/

easyQuestions = {
    "question1" : 10,
    "question2" : 20,
    "question3" : 30,
    "question4" : 40
}
mediumQuestions = { 
    "question" : 10,
    "question" : 20,
    "question" : 30,
    "question" : 40
}
hardQuestions = { 
    "question" : 10,
    "question" : 20,
    "question" : 30,
    "question" : 40
}

incompleteAnswerList = [random.randint(0, 34), random.randint(0, 34), random.randint(0, 34)]

# \/ Declaring Functions \/

def getQuestion(questions):
        n = random.randint(0,len(questions)-1)
        for i, key in enumerate(questions.keys()):
            if i == n:
                return key
            
def getAnswer(questionDict, key):
    answer = questionDict[key]
    return answer            

def whereInsertRealAnswer():
    randomIndex = random.randint(0,3)
    return randomIndex

def getAnswerChoices(randomIndex, answer, incompleteAnswerList):
    incompleteAnswerList.insert(randomIndex, answer)
    return incompleteAnswerList

def getElapsedTime(startTime, endTime):
    elapsedTime = math.floor(endTime - startTime)
    return elapsedTime

def calculateCritical(critTime, elapsedTime):
    if int(critTime) >= elapsedTime:
        criticalHit = True

    else:
        criticalHit = False

    return criticalHit

def isCorrect(playerAnswer):
     
     match playerAnswer.lower():

        case 'a':
            if answerChoices[0] == answerChoices[answerIndex]:
                correct = True
            else:
                correct = False
        
        case 'b':
            if answerChoices[1] == answerChoices[answerIndex]:
                correct = True
            else:
                correct = False

        case 'c':
            if answerChoices[2] == answerChoices[answerIndex]:
                correct = True
            else:
                correct = False

        case 'd':
            if answerChoices[3] == answerChoices[answerIndex]:
                correct = True
            else:
                correct = False

            
playerCharacter = namedtuple('playerCharacter',['name','race', 'attack', 'health', 'critTime']) # Creates "mould" for character object; allows us to map characteristics to character name

playerStartInput = input("Welcome to Fantasy Math Adventure!\n\nTo play, type: \'Go\' \nTo quit, type: \'q\'\n") # Gotta start off the while loop ;) "start menu"


while playerStartInput != 'q': # While loop keeps game going til player "quits"

# \/ Charcter Selection Walkthrough \/

    print("\nThis is the Character Selecter. Each character has unique abilities, ranging from different healths, to crit times, to special powers.\n")
    time.sleep(6) # From imported 'time' module; counts specified seconds before executing next line of code; makes the program look cooler 
    print("A creature's health determinds how much damage it can take, while its crit time is how long you can take to answer a question correctly and still deal critical damage.\n")
    time.sleep(6)
    print("To select your character, type the number by your character's name:\n")
    time.sleep(4)

    print("1. Name: Rush\n   Race: Elf\n   Attack: 5\n   Health: 8\n   Crit time: 10 Seconds\n")
    print("2. Name: Samson\n   Race: Hobbit\n   Attack: 7\n   Health: 10\n   Crit time: 7 Seconds\n")
    print("3. Name: Rog\n   Race: Orc\n   Attack: 8\n   Health: 12\n   Crit time: 5 Seconds\n")

# \/ Creates objects for each character \/ 

    rush = playerCharacter('Rush','Elf', '5', '8','10')
    samson = playerCharacter('Samson','Hobbit', '7', '10','7')
    rog = playerCharacter('Rog','Orc','8', '12','5')

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

# \/ Prints character selection by calling the 'name' value from the corresponding namedtuple \/

    time.sleep(2)
    print(f'Awesome! You chose {character.name}!')    

# \/ Checks if ready to start game; if no, quit game \/

    start = input("Are you ready to begin? (Yes or No)\n\n")

    if start.lower() == "no":
        print("Okay. Good bye :(")
        quit()

    else:
        print("Let's go!!\n")

# \/ Start Adventure \/



# \/ First Combat \/

    # insert enemy ascii art

    print('Oh no! There\'s an enemy ahead!') 
    time.sleep(4)
    print('To attack, answer the given question correctly.')
    time.sleep(4)
    print(f'To slay him in one hit, answer the question within {character.critTime} seconds. Ready?\n')
    time.sleep(4)
            
    question = getQuestion(easyQuestions) # Gets question randomly from dictionary
    answer = getAnswer(easyQuestions, question) # Gets answer based on initial dictionary/key
    answerIndex = whereInsertRealAnswer() # Stores where the answer was inserted in answer choices list
    answerChoices = getAnswerChoices(answerIndex, answer, incompleteAnswerList) # Gives list of answer choices w the real answer inserted randomly

    print(question) # Prints question
    print(f'\n\tA) {answerChoices[0]}\n\tB) {answerChoices[1]}\n\tC) {answerChoices[2]}\n\tD) {answerChoices[3]}\n\n') # Prints answer choices
    startTime = time.time() # Start timer
    playerAnswer = input() # Takes answer input
    endTime = time.time() # End timer

    timeTakenToAnswer = getElapsedTime(startTime, endTime) # Calculate elapsed time
 
# \/ Checks if answer was true; if so, critical hit? \/

    if isCorrect(playerAnswer) == True:
        if calculateCritical(playerCharacter.critTime, timeTakenToAnswer) == True:
            print(f'You correctly answered the question in {timeTakenToAnswer} seconds! That\'s a CRITICAL HIT! ')
        else:
            print(f'You correctly answered the question in {timeTakenToAnswer} seconds! You deal {playerCharacter.attack} damage!')
    else:
        print("Oh no! Your answer was incorrect! Try one more time...if you get it wrong, you will be defeated!")
        playerAnswer = input()
        if isCorrect(playerAnswer) == True: # Player deals half damage if correct on the second try
            halfDamage = int(playerCharacter.attack)//2
            print(f"You did it! {halfDamage} damage was dealt and you avoided taking damage.")
        else: # Player dies if incorrect on the second try
            print("Oh no! You were defeated! Better luck next time...")
            quit()


    

