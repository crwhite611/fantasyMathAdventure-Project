# This is an awesome python project written and designed by LJ, Nathan, and Callie

from collections import namedtuple
import time # Allows use of sleep function; makes the program look cooler
import random
import math

# \/ Declare question dictionaries here; problem mapped to answer \/

easyQuestions = {
    "2+17" : 19,
    "12*4" : 48,
    "74-18" : 56,
    "89+21" : 110,
    "13-17" : -4,
    "2+16" : 18,
    "15+4" : 19,
    "12-18" : -6,
    "13*2" : 26,
    "14-9" : 5
}
mediumQuestions = { 
    "-3+2x=11" : 7,
    "4x+6=-10" : -4,
    "x+9=18-2x" : 3,
    "2x+6=4x-2" : 4,
    "15+5x=0" : -74,
    "17x-12=114+3x" : 9,
    "12x+0=144" : 12,
    "-10x-19=19-8x" : -19
}
hardQuestions = { 
    "6/2(1+2)" : 9,
    "7-24/8*4+6" : 1,
    "18/3-7+2*5" : 9,
    "51/17-4+6(2*3)" : 35 
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
    
    if critTime >= elapsedTime:
        criticalHit = True

    else:
        criticalHit = False

    return criticalHit

def isCorrect(playerAnswer):
     
     match playerAnswer.lower():

        case 'a':
            if answerChoices[0] == answerChoices[answerIndex]:
                correct = True
                return correct
                
            else:
                correct = False
                return correct
        
        case 'b':
            if answerChoices[1] == answerChoices[answerIndex]:
                correct = True
                return correct
            
            else:
                correct = False
                return correct

        case 'c':
            if answerChoices[2] == answerChoices[answerIndex]:
                correct = True
                return correct
            
            else:
                correct = False
                return correct

        case 'd':
            if answerChoices[3] == answerChoices[answerIndex]:
                correct = True
                return correct
            
            else:
                correct = False
                return correct

# \/ Creates class for character object; allows us to map characteristics to character name \/

class PlayerCharacter:

    def __init__(self, name, race, attack, health, critTime):

        self.name = name
        self.race = race
        self.attack = attack
        self.health = health
        self.critTime = critTime

    def dealHalfDamage(self, enemyHealth, attack):
        enemyHealth -= (attack//2)

    def dealFullDamage(self, enemyHealth, attack):
        enemyHealth -= attack

# \/ Creates class for enemy object

class Enemy:

    def __init__(self, attack, health):
        self.attacak = attack
        self.health = health

    def dealDamage(self, attack, playerHealth):
        playerHealth -= attack

# \/ Create enemies \/

evilWizardRidingDragon = Enemy(7, 20)
redDragon = Enemy(6, 15)
blueDragon = Enemy(5, 12)
ogre = Enemy(3, 10)
kobold = Enemy(4, 8)



playerStartInput = input("Welcome to Fantasy Math Adventure!\n\nTo play, type: \'Go\' \nTo quit, type: \'q\'\n") # Gotta start off the while loop ;) "start menu"


while playerStartInput != 'q': # While loop keeps game going til player "quits"

# \/ Charcter Selection Walkthrough \/

    print("\nThis is the Character Selecter. Each character has unique abilities, ranging from different healths, to crit times, to special powers.\n")
    #time.sleep(6) # From imported 'time' module; counts specified seconds before executing next line of code; makes the program look cooler 
    print("A creature's health determinds how much damage it can take, while its crit time is how long you can take to answer a question correctly and still deal critical damage.\n")
    #time.sleep(6)
    print("To select your character, type the number by your character's name:\n")
    #time.sleep(4)

    print("1. Name: Rush\n   Race: Elf\n   Attack: 5\n   Health: 8\n   Crit time: 10 Seconds\n")
    print("2. Name: Samson\n   Race: Hobbit\n   Attack: 7\n   Health: 10\n   Crit time: 7 Seconds\n")
    print("3. Name: Rog\n   Race: Orc\n   Attack: 8\n   Health: 12\n   Crit time: 5 Seconds\n")

# \/ Creates objects for each character \/ 

    rush = PlayerCharacter('Rush','Elf', 5, 8, 7)
    samson = PlayerCharacter('Samson','Hobbit', 7, 10, 5)
    rog = PlayerCharacter('Rog','Orc', 8, 12, 4)

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

    print(f'\nAwesome! You chose {character.name}!')    

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

    print('Oh no! There\'s an enemy Ogre ahead!') 
    #time.sleep(4)
    print('\nTo attack, answer the given question correctly.')
    #time.sleep(4)
    print(f'\nTo slay him in one hit, answer the question within {character.critTime} seconds. Ready?\n')
    #time.sleep(4)
            
    question = getQuestion(easyQuestions) # Gets question randomly from dictionary
    answer = getAnswer(easyQuestions, question) # Gets answer based on initial dictionary/key
    answerIndex = whereInsertRealAnswer() # Stores where the answer was inserted in answer choices list
    answerChoices = getAnswerChoices(answerIndex, answer, incompleteAnswerList) # Gives list of answer choices w the real answer inserted randomly

    print(question) # Prints question
    print(f'\n   A) {answerChoices[0]}\n   B) {answerChoices[1]}\n   C) {answerChoices[2]}\n   D) {answerChoices[3]}\n\n') # Prints answer choices
    startTime = time.time() # Start timer
    playerAnswer = input() # Takes answer input
    endTime = time.time() # End timer

    timeTakenToAnswer = getElapsedTime(startTime, endTime) # Calculate elapsed time
    time.sleep(2)
 
# \/ Checks if answer was true; if so, critical hit? \/

    if isCorrect(playerAnswer) == True:
        if calculateCritical(character.critTime, timeTakenToAnswer) == True:
            print(f'\nYou correctly answered the question in {timeTakenToAnswer} seconds! That\'s a CRITICAL HIT! ')

# \/ If non-lethal was dealt, asks another question so you can deal full damage \/

        else: 
            print(f'\nYou correctly answered the question in {timeTakenToAnswer} seconds! You deal {character.attack} damage!')
            character.dealFullDamage(ogre.health, character.attack)
            print("Good job, but he is still alive! Answer the next question correctly to finish him!")

            question = getQuestion(easyQuestions) # Gets second question randomly from dictionary
            answer = getAnswer(easyQuestions, question) # Gets answer based on initial dictionary/key
            answerIndex = whereInsertRealAnswer() # Stores where the answer was inserted in answer choices list
            answerChoices = getAnswerChoices(answerIndex, answer, incompleteAnswerList) # Gives list of answer choices w the real answer inserted randomly

            print(question) # Prints question
            print(f'\n   A) {answerChoices[0]}\n   B) {answerChoices[1]}\n   C) {answerChoices[2]}\n   D) {answerChoices[3]}\n\n') # Prints answer choices
            startTime = time.time() # Start timer
            playerAnswer = input() # Takes answer input
            endTime = time.time() # End timer

            timeTakenToAnswer = getElapsedTime(startTime, endTime) # Calculate elapsed time
            time.sleep(2)

# \/ Check if second answer was correct \/

            if calculateCritical(character.critTime, timeTakenToAnswer) == True:
                print(f'\nYou correctly answered the question and defeated the enemy! Way to go!')

            else:
                print("\nOh no! Your answer was incorrect! Try one more time...if you get it wrong, you will be defeated!")
                playerAnswer = input()

                if isCorrect(playerAnswer) == True: # Player deals half damage if correct on the second try
                    print(f"\nYou did it! {character.attack} damage was dealt and you avoided taking damage.")

                else: # Player dies if incorrect on the second try
                    print("\nOh no! You were defeated! Better luck next time...")
                    quit()

    else:
        print("\nOh no! Your answer was incorrect! Try one more time...if you get it wrong, you will be defeated!")
        playerAnswer = input()
        
        if isCorrect(playerAnswer) == True: # Player deals half damage if correct on the second try
            print(f"\nYou did it! {character.attack} damage was dealt and you avoided taking damage.")

        else: # Player dies if incorrect on the second try
            print("\nOh no! You were defeated! Better luck next time...")
            quit()

    
