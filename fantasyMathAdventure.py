# This is an awesome python project written and designed by LJ, Nathan, and Callie

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

completionTime = 0 # Total time taken to complete game

# \/ Start Program \/

playerStartInput = input("Welcome to Fantasy Math Adventure!\n\nTo play, type: \'Go\' \nTo quit, type: \'q\'\n") # Gotta start off the while loop ;) "start menu"

while True:

    if playerStartInput.lower() == 'go':
        break
    elif playerStartInput.lower() == 'q':
        print("Alright, see you next time!")
        quit()  # exit the loop
    else:
        playerStartInput = input("Invalid input. Please enter 'Go' or 'q'.")


while playerStartInput != 'q': # While loop keeps game going til player "quits"

# \/ Charcter Selection Walkthrough \/

    print("\nThis is the Character Selecter. Each character has unique abilities, including different healths and crit times.\n")
    time.sleep(6) # From imported 'time' module; counts specified seconds before executing next line of code; makes the program look cooler 
    print("A creature's health determinds how much damage it can take, while its crit time is how long you can take to answer a question correctly and still deal critical damage.\n")
    time.sleep(6)
    print("To select your character, type the number by your character's name:\n")
    time.sleep(4)

    print("1. Name: Rush\n   Race: Elf\n   Attack: 5\n   Health: 8\n   Crit time: 10 Seconds\n")
    print("2. Name: Samson\n   Race: Hobbit\n   Attack: 7\n   Health: 10\n   Crit time: 7 Seconds\n")
    print("3. Name: Rog\n   Race: Orc\n   Attack: 8\n   Health: 12\n   Crit time: 5 Seconds\n")

# \/ Creates objects for each character \/ 

    rush = PlayerCharacter('Rush','Elf', 5, 8, 7)
    samson = PlayerCharacter('Samson','Hobbit', 7, 10, 5)
    rog = PlayerCharacter('Rog','Orc', 8, 12, 4)

# \/ Take input for character selection \/

    characterSelection = input("Enter a character selection (1, 2, 3): \n\n")

    while True:

        if characterSelection == '1':
            break
        elif characterSelection == '2':
            break
        elif characterSelection == '3':
            break
        else:
            characterSelection = input("Invalid input. Please enter 1, 2, or 3.\n\n")
    

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

    user_input = input("Are you ready to begin? (Yes/No): ")

    while True:

        if user_input.lower() == 'yes':
            break
        elif user_input.lower() == 'no':
            print("Alright, see you next time!")
            quit() 
        else:
            user_input = input("\nInvalid input. Please enter 'Yes' or 'No'.\n\n")
# \/ Start Adventure \/
    print(".\n")
    print(".\n")
    print(".\n\n")

    print("\nThe night is quiet and peaceful. The sky is cloudless, and moonlight illuminates the dark ground below.\n")
    time.sleep(5)
    print("You are on your way home from the local restaurant after a rare meal out. Beside you walks your younger sister.\n")
    time.sleep(5)
    print("You look down at her with a smile. Life was not easy, but you were content.\n")
    print("\n")
    time.sleep(5)
    

    print("As you continue to walk, you notice the lack of people on the street.\n")
    time.sleep(5)
    print("It was starting to get late, so it was not strange that there were not a lot of people, but you still would have expected to see a few more.\n")
    time.sleep(7)
    print("A feeling of unease begins to settle over you.\n")
    time.sleep(5)

    print("Rumors that the infamous Black Dagger Gang had been abducting people were circulating through the city.\n")
    time.sleep(5)
    print("With that in mind, having so few people around put you on edge.\n")
    time.sleep(5)

    print("As you pass an alleyway, you hear a scraping sound behind you, as if boots had been dragged against the stone street.\n")
    time.sleep(5)
    print("You turn your head to look for the source of the noise, but see nothing.\n")
    time.sleep(5)

    print("As soon as your head is turned, however, you hear the sudden sound of rapid footsteps.\n")
    time.sleep(4)
    print("Your head snaps back forward just in time to see a man rushing toward you.\n")
    time.sleep(4)
    print("He throws a punch at you, but you avoid it and jump backwards.\n")
    time.sleep(4)
    print("You do not know who this man is, but you can tell that he is not friendly.\n")
    time.sleep(4) 
    print("He seems intent on harming you, so you must defend yourself.\n\n\n\n")
    time.sleep(4)


# \/ First Combat \/

    print('**Defeat the unknown man.') 
    time.sleep(4)
    print('\n**To attack, answer the given question correctly.')
    time.sleep(4)
    print(f'\n**To slay him in one hit, answer the question within {character.critTime} seconds. Ready?\n')
    time.sleep(4)
            
    question = getQuestion(easyQuestions) # Gets question randomly from dictionary
    answer = getAnswer(easyQuestions, question) # Gets answer based on initial dictionary/key
    answerIndex = whereInsertRealAnswer() # Stores where the answer was inserted in answer choices list
    answerChoices = getAnswerChoices(answerIndex, answer, incompleteAnswerList) # Gives list of answer choices w the real answer inserted randomly

    print(question) # Prints question
    print(f'\n   A) {answerChoices[0]}\n   B) {answerChoices[1]}\n   C) {answerChoices[2]}\n   D) {answerChoices[3]}\n\n') # Prints answer choices
    startTime = time.time() # Start timer
    
    playerAnswer = input() # Takes answer input
    
    while True:

        if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
            break
        else:
            playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

    endTime = time.time() # End timer

    timeTakenToAnswer = getElapsedTime(startTime, endTime) # Calculate elapsed time
    completionTime += timeTakenToAnswer
    time.sleep(2)
 
# \/ Checks if answer was true; if so, critical hit? \/

    if isCorrect(playerAnswer) == True:
        if calculateCritical(character.critTime, timeTakenToAnswer) == True:
            print(f'\nYou correctly answered the question in {timeTakenToAnswer} seconds! That\'s a CRITICAL HIT! ')

# \/ If non-lethal was dealt, asks another question so you can deal full damage \/

        else: 
            print(f'\nYou correctly answered the question in {timeTakenToAnswer} seconds! You deal {character.attack} damage!')
            print("Good job, but he is still alive! Answer the next question correctly to finish him!")

            question = getQuestion(easyQuestions) # Gets second question randomly from dictionary
            answer = getAnswer(easyQuestions, question) # Gets answer based on initial dictionary/key
            answerIndex = whereInsertRealAnswer() # Stores where the answer was inserted in answer choices list
            answerChoices = getAnswerChoices(answerIndex, answer, incompleteAnswerList) # Gives list of answer choices w the real answer inserted randomly

            print(question) # Prints question
            print(f'\n   A) {answerChoices[0]}\n   B) {answerChoices[1]}\n   C) {answerChoices[2]}\n   D) {answerChoices[3]}\n') # Prints answer choices
            startTime = time.time() # Start timer
            playerAnswer = input() # Takes answer input

            while True:

                if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                    break
                else:
                    playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

            endTime = time.time() # End timer

            timeTakenToAnswer = getElapsedTime(startTime, endTime) # Calculate elapsed time
            completionTime += timeTakenToAnswer
            time.sleep(2)

# \/ Check if second answer was correct \/

            if calculateCritical(character.critTime, timeTakenToAnswer) == True:
                print(f'\nYou correctly answered the question and defeated the enemy! Way to go!')

            else:
                print("\nOh no! Your answer was incorrect! Try one more time...if you get it wrong, you will be defeated!")
                
                playerAnswer = input()

                while True:

                    if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                        break
                    else:
                        playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

                if isCorrect(playerAnswer) == True: # Player deals half damage if correct on the second try
                    print(f"\nYou did it! {character.attack} damage was dealt and you avoided taking damage.")

                else: # Player dies if incorrect on the second try
                    print("\nOh no! You were defeated! Better luck next time...")
                    quit()

    else:
        print("\nOh no! Your answer was incorrect! Try one more time...if you get it wrong, you will be defeated!")
        playerAnswer = input() # Takes answer input

        while True:

            if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                break
            else:
                playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")
        
        if isCorrect(playerAnswer) == True: # Player deals half damage if correct on the second try
            print(f"\nYou did it! {character.attack} damage was dealt and you avoided taking damage.")

        else: # Player dies if incorrect on the second try
            print("\nOh no! You were defeated! Better luck next time...")
            quit()

     # \/ First post-combat text \/
 
    print("\nYou stand over the man, wondering who he is as you try to catch your breath.\n")
    time.sleep(5)

    print("Suddenly, you hear your sister scream. Your head snaps to the side and you see another man dragging your sister away.\n")
    time.sleep(4)
    print("You take a step towards them, but abruptly stop as you feel a sharp pain sprout in the back of your head.\n")
    time.sleep(3)
    print('A loud “crack!” echoes through the streets as you are struck on the back of your head. Your vision begins to darken and you realize that you are falling over.\n')
    time.sleep(4)
    print("As you hit the ground, you catch a glimpse of your sister being dragged away before blacking out completely...\n\n\n\n")
    time.sleep(5)


# \/ Transition Text 1 \/

    print("When you come to, it is already morning. You are initially confused, managing to get to your feet but wobbling as you do so.\n")
    time.sleep(6)
    print("A sharp ache shoots through your head and you clutch it in pain. Memories from the night before flood back into your head, and your heart drops.\n")
    time.sleep(6)
    print("You look around in a panic, ignoring the pain in your head. You call your sister\'s name frantically, hoping that your memories were wrong.\n")
    time.sleep(6)
    print("A few passerby give you strange looks as they walk by you, but you pay them no heed.\n")
    time.sleep(6)
    print("You pause for a moment, hoping and praying that your sister will come running to you, as she always does.\n")
    time.sleep(3)
    print(".\n")
    time.sleep(2)
    print(".\n")
    time.sleep(2)
    print(".\n")
    time.sleep(2)
    print("But that doesn\'t happen this time.\n\n\n")
    time.sleep(7)


    print("You stumble, struggling to stand as you are overcome by fear and worry.\n")
    time.sleep(5)
    print("How could this have happened? What were you going to do now?\n")
    time.sleep(3)
    print("These thoughts ran rampant in your mind.\n\n")
    time.sleep(6)
    print("Then you remembered something.\n")
    time.sleep(5)
    print("The rumors about the Black Dagger Gang came back to you. Maybe they were responsible this time too.\n")
    time.sleep(4)
    print("Maybe they knew where your sister had been taken.\n")
    time.sleep(5)
    print("You had heard that the leader of the gang, Gyle, frequented a nearby tavern.\n")
    time.sleep(4)
    print("If the Black Daggers really were responsible, then he would surely know the whereabouts of your sister.\n")
    time.sleep(3)

    print(".\n")
    time.sleep(2)
    print(".\n")
    time.sleep(2)
    print(".\n\n")
    time.sleep(2)

    print("\nYou stand outside the tavern. You feel nervousness welling up inside of you, but you quickly squash it down.\n") 
    time.sleep(5)
    print("You harden your resolve and open the door.\n")
    time.sleep(5)
    print("The people inside are the rough sort, almost every one of them involved with crime to some degree. They glare at you, and you glare back.\n")
    time.sleep(5)
    print("Normally, you would have steered clear of them, but that was not an option this time.\n\n")
    time.sleep(5)
    print("You scan the interior of the tavern and your eyes are drawn to a particular patron.\n")
    time.sleep(5)
    print("The people around him seem nervous, as if they are uncomfortable being around him. Yet, they seem to treat him with respect and deference.\n")
    time.sleep(5)
    print("Instinctively, you realize that this must be the person you are looking for.\n") 
    time.sleep(5)
    print("To the surprise and horror of the other patrons, you take a step toward him. He looks at you evenly, slightly curious but otherwise unbothered.\n\n")
    time.sleep(5)

    print('"Are you the leader of the Black Dagger Gang?” You ask.\n')
    time.sleep(5)
    print('"Who\'s asking?” the man responds.\n')
    time.sleep(4)
    print("Your fists clench in anger.\n")
    time.sleep(4)
    print('"Where are the people you kidnapped?” You demand, raising your voice.\n')
    time.sleep(4)
    print('The man smiles. "Oh, I see. You\'re related to one of them. Well, it would be best for you to just forget about them. They\'re probably already dead.”\n')
    time.sleep(6)
    print('“You will tell me, one way or another,” you snarl. The man\'s smile widens.\n')
    time.sleep(5)
    print('“Yeah? Try and make me.”\n\n\n\n')
    time.sleep(5)


# \/ Second Combat \/

    print('\nTo attack, answer the given question correctly.')
    time.sleep(4)
    print(f'\nTo slay him in one hit, answer the question within {character.critTime} seconds. Ready?\n')
    time.sleep(4)
            
    question = getQuestion(easyQuestions) # Gets question randomly from dictionary
    answer = getAnswer(easyQuestions, question) # Gets answer based on initial dictionary/key
    answerIndex = whereInsertRealAnswer() # Stores where the answer was inserted in answer choices list
    answerChoices = getAnswerChoices(answerIndex, answer, incompleteAnswerList) # Gives list of answer choices w the real answer inserted randomly

    print(question) # Prints question
    print(f'\n   A) {answerChoices[0]}\n   B) {answerChoices[1]}\n   C) {answerChoices[2]}\n   D) {answerChoices[3]}\n\n') # Prints answer choices
    startTime = time.time() # Start timer
    
    playerAnswer = input() # Takes answer input
    
    while True:

        if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
            break
        else:
            playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

    endTime = time.time() # End timer

    timeTakenToAnswer = getElapsedTime(startTime, endTime) # Calculate elapsed time
    completionTime += timeTakenToAnswer
    time.sleep(2)
 
# \/ Checks if answer was true; if so, critical hit? \/

    if isCorrect(playerAnswer) == True:
        if calculateCritical(character.critTime, timeTakenToAnswer) == True:
            print(f'\nYou correctly answered the question in {timeTakenToAnswer} seconds! That\'s a CRITICAL HIT! ')

# \/ If non-lethal was dealt, asks another question so you can deal full damage \/

        else: 
            print(f'\nYou correctly answered the question in {timeTakenToAnswer} seconds! You deal {character.attack} damage!')
            print("Good job, but he is still alive! Answer the next question correctly to finish him!")

            question = getQuestion(easyQuestions) # Gets second question randomly from dictionary
            answer = getAnswer(easyQuestions, question) # Gets answer based on initial dictionary/key
            answerIndex = whereInsertRealAnswer() # Stores where the answer was inserted in answer choices list
            answerChoices = getAnswerChoices(answerIndex, answer, incompleteAnswerList) # Gives list of answer choices w the real answer inserted randomly

            print(question) # Prints question
            print(f'\n   A) {answerChoices[0]}\n   B) {answerChoices[1]}\n   C) {answerChoices[2]}\n   D) {answerChoices[3]}\n') # Prints answer choices
            startTime = time.time() # Start timer
            playerAnswer = input() # Takes answer input

            while True:

                if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                    break
                else:
                    playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

            endTime = time.time() # End timer

            timeTakenToAnswer = getElapsedTime(startTime, endTime) # Calculate elapsed time
            completionTime += timeTakenToAnswer
            time.sleep(2)

# \/ Check if second answer was correct \/

            if calculateCritical(character.critTime, timeTakenToAnswer) == True:
                print(f'\nYou correctly answered the question and defeated the enemy! Way to go!')

            else:
                print("\nOh no! Your answer was incorrect! Try one more time...if you get it wrong, you will be defeated!")
                
                playerAnswer = input()

                while True:

                    if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                        break
                    else:
                        playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

                if isCorrect(playerAnswer) == True: # Player deals half damage if correct on the second try
                    print(f"\nYou did it! {character.attack} damage was dealt and you avoided taking damage.")

                else: # Player dies if incorrect on the second try
                    print("\nOh no! You were defeated! Better luck next time...")
                    quit()

    else:
        print("\nOh no! Your answer was incorrect! Try one more time...if you get it wrong, you will be defeated!")
        playerAnswer = input() # Takes answer input

        while True:

            if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                break
            else:
                playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")
        
        if isCorrect(playerAnswer) == True: # Player deals half damage if correct on the second try
            print(f"\nYou did it! {character.attack} damage was dealt and you avoided taking damage.")

        else: # Player dies if incorrect on the second try
            print("\nOh no! You were defeated! Better luck next time...")
            quit()

# \/ Second post-combat text \/


    print("The gang leader stumbles back, struggling to stand. You prepare to attack him again, but he raises his hands in surrender.\n")
    time.sleep(5)
    print('“Fine, fine! I\'ll tell you where they are!” He says hurriedly. You relax slightly.\n')
    time.sleep(5)
    print('“Tell me!” You demand.\n')
    time.sleep(4)
    print('“I can\'t believe I lost to some nobody like you…” Gyle mumbles before taking a breath.\n')
    time.sleep(5)
    print('“I don\'t have them anymore. I sold them to those bandits in the Southend Mountains.”\n')
    time.sleep(5)
    print('Your heart drops. “What? Why? What would bandits want with those people?”\n')
    time.sleep(5)
    print('Gyle shrugs. “I don\'t know. It was just business, I didn\'t ask.”\n')
    time.sleep(5)
    print('You growl in frustration. “Tell me where exactly those bandits are.”\n\n')
    time.sleep(5)

    print('The defeated gang leader looks at another nearby man, who had been watching the fight. The man immediately runs into a back room of the tavern.\n')
    time.sleep(7)
    print('After a moment, he comes back out with a rolled-up piece of paper in his hands. He hands it to Gyle, who then hands it to you.\n')
    time.sleep(7)
    print('“That\'s the map I gave my guys when they went to make the deal. It shows the location of the bandit hideout.”\n')
    time.sleep(6)
    print("You unroll the map. It shows the city and the surrounding areas, including the Southend Mountains. There is a small \'x\' over a specific spot in the mountains.\n")
    time.sleep(8)
    print("You turn and leave the tavern, and then the city entirely.\n\n\n\n")
    time.sleep(3)

    print(".\n")
    time.sleep(2)
    print(".\n")
    time.sleep(2)
    print(".\n")
    time.sleep(2)
    


# \/ End part 1 \/

# \/ Part 2/3, Journey South \/



# \/ Transition Text 2 \/

    print("After just a few hours of walking, you have reached the northern edge of the mountains.\n")
    time.sleep(5)
    print("You spot a path that seems to go in the same direction you need to go. You step onto the path to continue your journey.\n")
    time.sleep(6)
    print("After just a few more minutes of walking, you hear a rustling sound coming from the foliage at the side of the path. You raise your guard, unsure of what it it.\n")
    time.sleep(8)
    print("Could it be one of the bandits?\n\n")
    time.sleep(5)
    print("That question was answered when a large figure stepped onto the path.\n")
    time.sleep(5)
    print("It was a massive ogre.\n")
    time.sleep(4)
    print("Drool dripped from its mouth as it stalked forward, searching for its next meal.\n")
    time.sleep(5)
    print("The ogre stops as it spots you, standing up straight as a sinister grin crosses its face. It towers over you.\n")
    time.sleep(6)
    print("It lets out a thundering roar.\n")
    time.sleep(3)
    print('“RAAAAAAAARGH!”\n\n\n')
    time.sleep(5)
    print("You prepare for battle.\n\n\n\n")


# \/ Third Combat \/

    print('\nTo attack, answer the given question correctly.')
    time.sleep(4)
    print(f'\nTo slay him in one hit, answer the question within {character.critTime} seconds. Ready?\n')
    time.sleep(4)
            
    question = getQuestion(easyQuestions) # Gets question randomly from dictionary
    answer = getAnswer(easyQuestions, question) # Gets answer based on initial dictionary/key
    answerIndex = whereInsertRealAnswer() # Stores where the answer was inserted in answer choices list
    answerChoices = getAnswerChoices(answerIndex, answer, incompleteAnswerList) # Gives list of answer choices w the real answer inserted randomly

    print(question) # Prints question
    print(f'\n   A) {answerChoices[0]}\n   B) {answerChoices[1]}\n   C) {answerChoices[2]}\n   D) {answerChoices[3]}\n\n') # Prints answer choices
    startTime = time.time() # Start timer
    
    playerAnswer = input() # Takes answer input
    
    while True:

        if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
            break
        else:
            playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

    endTime = time.time() # End timer

    timeTakenToAnswer = getElapsedTime(startTime, endTime) # Calculate elapsed time
    completionTime += timeTakenToAnswer
    time.sleep(2)
 
# \/ Checks if answer was true; if so, critical hit? \/

    if isCorrect(playerAnswer) == True:
        if calculateCritical(character.critTime, timeTakenToAnswer) == True:
            print(f'\nYou correctly answered the question in {timeTakenToAnswer} seconds! That\'s a CRITICAL HIT! ')

# \/ If non-lethal was dealt, asks another question so you can deal full damage \/

        else: 
            print(f'\nYou correctly answered the question in {timeTakenToAnswer} seconds! You deal {character.attack} damage!')
            print("Good job, but he is still alive! Answer the next question correctly to finish him!")

            question = getQuestion(easyQuestions) # Gets second question randomly from dictionary
            answer = getAnswer(easyQuestions, question) # Gets answer based on initial dictionary/key
            answerIndex = whereInsertRealAnswer() # Stores where the answer was inserted in answer choices list
            answerChoices = getAnswerChoices(answerIndex, answer, incompleteAnswerList) # Gives list of answer choices w the real answer inserted randomly

            print(question) # Prints question
            print(f'\n   A) {answerChoices[0]}\n   B) {answerChoices[1]}\n   C) {answerChoices[2]}\n   D) {answerChoices[3]}\n') # Prints answer choices
            startTime = time.time() # Start timer
            playerAnswer = input() # Takes answer input

            while True:

                if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                    break
                else:
                    playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

            endTime = time.time() # End timer

            timeTakenToAnswer = getElapsedTime(startTime, endTime) # Calculate elapsed time
            completionTime += timeTakenToAnswer
            time.sleep(2)

# \/ Check if second answer was correct \/

            if calculateCritical(character.critTime, timeTakenToAnswer) == True:
                print(f'\nYou correctly answered the question and defeated the enemy! Way to go!')

            else:
                print("\nOh no! Your answer was incorrect! Try one more time...if you get it wrong, you will be defeated!")
                
                playerAnswer = input()

                while True:

                    if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                        break
                    else:
                        playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

                if isCorrect(playerAnswer) == True: # Player deals half damage if correct on the second try
                    print(f"\nYou did it! {character.attack} damage was dealt and you avoided taking damage.")

                else: # Player dies if incorrect on the second try
                    print("\nOh no! You were defeated! Better luck next time...")
                    quit()

    else:
        print("\nOh no! Your answer was incorrect! Try one more time...if you get it wrong, you will be defeated!")
        playerAnswer = input() # Takes answer input

        while True:

            if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                break
            else:
                playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")
        
        if isCorrect(playerAnswer) == True: # Player deals half damage if correct on the second try
            print(f"\nYou did it! {character.attack} damage was dealt and you avoided taking damage.")

        else: # Player dies if incorrect on the second try
            print("\nOh no! You were defeated! Better luck next time...")
            quit()

# ------------------------------------------------------------------Asks another series of questions------------------------------------------------------------------------

    question = getQuestion(mediumQuestions) # Gets question randomly from dictionary
    answer = getAnswer(mediumQuestions, question) # Gets answer based on initial dictionary/key
    answerIndex = whereInsertRealAnswer() # Stores where the answer was inserted in answer choices list
    answerChoices = getAnswerChoices(answerIndex, answer, incompleteAnswerList) # Gives list of answer choices w the real answer inserted randomly

    print(question) # Prints question
    print(f'\n   A) {answerChoices[0]}\n   B) {answerChoices[1]}\n   C) {answerChoices[2]}\n   D) {answerChoices[3]}\n\n') # Prints answer choices
    startTime = time.time() # Start timer
    
    playerAnswer = input() # Takes answer input
    
    while True:

        if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
            break
        else:
            playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

    endTime = time.time() # End timer

    timeTakenToAnswer = getElapsedTime(startTime, endTime) # Calculate elapsed time
    completionTime += timeTakenToAnswer
    time.sleep(2)
 
# \/ Checks if answer was true; if so, critical hit? \/

    if isCorrect(playerAnswer) == True:
        if calculateCritical(character.critTime, timeTakenToAnswer) == True:
            print(f'\nYou correctly answered the question in {timeTakenToAnswer} seconds! That\'s a CRITICAL HIT! ')

# \/ If non-lethal was dealt, asks another question so you can deal full damage \/

        else: 
            print(f'\nYou correctly answered the question in {timeTakenToAnswer} seconds! You deal {character.attack} damage!')
            print("Good job, but he is still alive! Answer the next question correctly to finish him!")

            question = getQuestion(mediumQuestions) # Gets second question randomly from dictionary
            answer = getAnswer(mediumQuestions, question) # Gets answer based on initial dictionary/key
            answerIndex = whereInsertRealAnswer() # Stores where the answer was inserted in answer choices list
            answerChoices = getAnswerChoices(answerIndex, answer, incompleteAnswerList) # Gives list of answer choices w the real answer inserted randomly

            print(question) # Prints question
            print(f'\n   A) {answerChoices[0]}\n   B) {answerChoices[1]}\n   C) {answerChoices[2]}\n   D) {answerChoices[3]}\n') # Prints answer choices
            startTime = time.time() # Start timer
            playerAnswer = input() # Takes answer input

            while True:

                if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                    break
                else:
                    playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

            endTime = time.time() # End timer

            timeTakenToAnswer = getElapsedTime(startTime, endTime) # Calculate elapsed time
            completionTime += timeTakenToAnswer
            time.sleep(2)

# \/ Check if second answer was correct \/

            if calculateCritical(character.critTime, timeTakenToAnswer) == True:
                print(f'\nYou correctly answered the question and defeated the enemy! Way to go!')

            else:
                print("\nOh no! Your answer was incorrect! Try one more time...if you get it wrong, you will be defeated!")
                
                playerAnswer = input()

                while True:

                    if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                        break
                    else:
                        playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

                if isCorrect(playerAnswer) == True: # Player deals half damage if correct on the second try
                    print(f"\nYou did it! {character.attack} damage was dealt and you avoided taking damage.")

                else: # Player dies if incorrect on the second try
                    print("\nOh no! You were defeated! Better luck next time...")
                    quit()

    else:
        print("\nOh no! Your answer was incorrect! Try one more time...if you get it wrong, you will be defeated!")
        playerAnswer = input() # Takes answer input

        while True:

            if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                break
            else:
                playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")
        
        if isCorrect(playerAnswer) == True: # Player deals half damage if correct on the second try
            print(f"\nYou did it! {character.attack} damage was dealt and you avoided taking damage.")

        else: # Player dies if incorrect on the second try
            print("\nOh no! You were defeated! Better luck next time...")
            quit()


# \/ Third post-combat text, only display this + following if player wins battle(?) \/

    print("The ogre lets out a low growl as it realizes that you are not as easy of a meal as it thought. Its posture is defensive, and it is clear that it sees you as a threat now.\n")
    time.sleep(10)
    print("You keep your guard up, ready to defend yourself if the ogre attacks again.\n")
    time.sleep(5)
    print("It becomes clear that you will not have to, however, as the ogre turns and runs away.\n")
    time.sleep(5)
    print("You let out a sigh of relief as the ogre leaves. You rest for a moment before continuing along the path.\n\n\n\n")
    time.sleep(3)

    print(".\n")
    time.sleep(2)
    print(".\n")
    time.sleep(2)
    print(".\n\n")
    time.sleep(2)
    


# \/ Transition text 3 \/


    print("Before long, you spot footprints. Reasoning that they were made by either the Black Dagger Gang or the mountain bandits, you follow them.\n")
    time.sleep(8)
    print("After following the path for a while longer, the footprints suddenly veer off the path. You continue to follow them.\n")
    time.sleep(6)
    print("After another hour or so, you begin to hear what sounds like voices. You slowly and carefully creep toward the source of the voices.\n")
    time.sleep(7)
    print("Soon, you come across a wooden fence. Just past it, you can make out a couple figures moving around. Following along the fence, you find a gap and squeeze through, entering the bandit hideout.\n")
    time.sleep(10)
    print("You make your way along the outskirts, doing your best to remain unseen. Luckily for you, the bandits seem to be in the midst of some sort of celebration. They all sit around a large fire, oblivious to your presence.\n\n")
    time.sleep(10)

    print("The camp is full of several small shelters, mostly in the form of tents made of sticks and animal hide. Eventually, you spot a larger shelter made of logs that you estimate to be about ten feet tall.\n")
    time.sleep(10)
    print("The large shelter must be the residence of the bandit chief, you reason. Surely the chief would know where your sister is being kept.\n")
    time.sleep(8)
    print("Slowly and carefully, you work your way toward the large shelter. You spot a few bandit guards along the way, but you make it to the shelter's entrance unnoticed.\n")
    time.sleep(10)
    print("You slip inside the shelter.\n\n")
    time.sleep(3)
    
    print(".\n")
    time.sleep(2)
    print(".\n")
    time.sleep(2)
    print(".\n\n")
    time.sleep(2)


    print("As soon as you step into the shelter, you feel eyes on you. You turn quickly to the left and are immediately on guard, feeling some sort of pressure coming from the other side of the room.\n")
    time.sleep(10)
    print("There, you spot a man sitting on a large chair. You recognize him from wanted posters you have seen in the city.\n")
    time.sleep(8)
    print("They call him Ernulf the Mountain King, and he is the most infamous bandit in the country.\n")
    time.sleep(6)
    print("You can tell that he is massive, as even sitting down he seems tall. He watches you, his expression a mixture of curiosity and well-hidden surprise.\n")
    time.sleep(8)
    print('“Who are you?” He asks, his voice low and rumbling. Even though his voice is calm and his posture is relaxed, he is incredibly intimidating.\n')
    time.sleep(8)
    print('“I\'m looking for my sister. The Black Dagger Gang in Llothric sold her to you.” You say\n')
    time.sleep(6)
    print('Ernulf looks at you for a second before responding. “I see,” he says. “Then you should turn back now. Your sister is most likely already dead.”\n')
    time.sleep(8)
    print('Your breath catches in your throat and it feels like your heart has stopped. “What did you do to her?” You demand, your voice low but threatening.\n')
    time.sleep(8)
    print('Ernulf does not say anything.\n')
    time.sleep(5)
    print('“Where is she!?” You continue, your voice louder than before.\n')
    time.sleep(5)
    print('Ernulf shakes his head. “You do not know what you are dealing with. If you continue along this path, you will die too.”\n')
    time.sleep(8)
    print('“You will tell me. I will make you.” You state coldly.\n')
    time.sleep(5)
    print("Ernulf stands up. He is even bigger than you expected, his head barely shorter than the ceiling. He shakes his head again, an expression almost like pity on his face.\n")
    time.sleep(10)
    print('“I warned you.”\n\n\n\n')


# \/ Fourth Combat \/

    print('\nTo attack, answer the given question correctly.')
    time.sleep(4)
    print(f'\nTo slay him in one hit, answer the question within {character.critTime} seconds. Ready?\n')
    time.sleep(4)
            
    question = getQuestion(mediumQuestions) # Gets question randomly from dictionary
    answer = getAnswer(mediumQuestions, question) # Gets answer based on initial dictionary/key
    answerIndex = whereInsertRealAnswer() # Stores where the answer was inserted in answer choices list
    answerChoices = getAnswerChoices(answerIndex, answer, incompleteAnswerList) # Gives list of answer choices w the real answer inserted randomly

    print(question) # Prints question
    print(f'\n   A) {answerChoices[0]}\n   B) {answerChoices[1]}\n   C) {answerChoices[2]}\n   D) {answerChoices[3]}\n\n') # Prints answer choices
    startTime = time.time() # Start timer
    
    playerAnswer = input() # Takes answer input
    
    while True:

        if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
            break
        else:
            playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

    endTime = time.time() # End timer

    timeTakenToAnswer = getElapsedTime(startTime, endTime) # Calculate elapsed time
    completionTime += timeTakenToAnswer
    time.sleep(2)
 
# \/ Checks if answer was true; if so, critical hit? \/

    if isCorrect(playerAnswer) == True:
        if calculateCritical(character.critTime, timeTakenToAnswer) == True:
            print(f'\nYou correctly answered the question in {timeTakenToAnswer} seconds! That\'s a CRITICAL HIT! ')

# \/ If non-lethal was dealt, asks another question so you can deal full damage \/

        else: 
            print(f'\nYou correctly answered the question in {timeTakenToAnswer} seconds! You deal {character.attack} damage!')
            print("Good job, but he is still alive! Answer the next question correctly to finish him!")

            question = getQuestion(mediumQuestions) # Gets second question randomly from dictionary
            answer = getAnswer(mediumQuestions, question) # Gets answer based on initial dictionary/key
            answerIndex = whereInsertRealAnswer() # Stores where the answer was inserted in answer choices list
            answerChoices = getAnswerChoices(answerIndex, answer, incompleteAnswerList) # Gives list of answer choices w the real answer inserted randomly

            print(question) # Prints question
            print(f'\n   A) {answerChoices[0]}\n   B) {answerChoices[1]}\n   C) {answerChoices[2]}\n   D) {answerChoices[3]}\n') # Prints answer choices
            startTime = time.time() # Start timer
            playerAnswer = input() # Takes answer input

            while True:

                if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                    break
                else:
                    playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

            endTime = time.time() # End timer

            timeTakenToAnswer = getElapsedTime(startTime, endTime) # Calculate elapsed time
            completionTime += timeTakenToAnswer
            time.sleep(2)

# \/ Check if second answer was correct \/

            if calculateCritical(character.critTime, timeTakenToAnswer) == True:
                print(f'\nYou correctly answered the question and defeated the enemy! Way to go!')

            else:
                print("\nOh no! Your answer was incorrect! Try one more time...if you get it wrong, you will be defeated!")
                
                playerAnswer = input()

                while True:

                    if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                        break
                    else:
                        playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

                if isCorrect(playerAnswer) == True: # Player deals half damage if correct on the second try
                    print(f"\nYou did it! {character.attack} damage was dealt and you avoided taking damage.")

                else: # Player dies if incorrect on the second try
                    print("\nOh no! You were defeated! Better luck next time...")
                    quit()

    else:
        print("\nOh no! Your answer was incorrect! Try one more time...if you get it wrong, you will be defeated!")
        playerAnswer = input() # Takes answer input

        while True:

            if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                break
            else:
                playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")
        
        if isCorrect(playerAnswer) == True: # Player deals half damage if correct on the second try
            print(f"\nYou did it! {character.attack} damage was dealt and you avoided taking damage.")

        else: # Player dies if incorrect on the second try
            print("\nOh no! You were defeated! Better luck next time...")
            quit()

# ------------------------------------------------------------------Asks another series of questions------------------------------------------------------------------------

    question = getQuestion(mediumQuestions) # Gets question randomly from dictionary
    answer = getAnswer(mediumQuestions, question) # Gets answer based on initial dictionary/key
    answerIndex = whereInsertRealAnswer() # Stores where the answer was inserted in answer choices list
    answerChoices = getAnswerChoices(answerIndex, answer, incompleteAnswerList) # Gives list of answer choices w the real answer inserted randomly

    print(question) # Prints question
    print(f'\n   A) {answerChoices[0]}\n   B) {answerChoices[1]}\n   C) {answerChoices[2]}\n   D) {answerChoices[3]}\n\n') # Prints answer choices
    startTime = time.time() # Start timer
    
    playerAnswer = input() # Takes answer input
    
    while True:

        if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
            break
        else:
            playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

    endTime = time.time() # End timer

    timeTakenToAnswer = getElapsedTime(startTime, endTime) # Calculate elapsed time
    completionTime += timeTakenToAnswer
    time.sleep(2)
 
# \/ Checks if answer was true; if so, critical hit? \/

    if isCorrect(playerAnswer) == True:
        if calculateCritical(character.critTime, timeTakenToAnswer) == True:
            print(f'\nYou correctly answered the question in {timeTakenToAnswer} seconds! That\'s a CRITICAL HIT! ')

# \/ If non-lethal was dealt, asks another question so you can deal full damage \/

        else: 
            print(f'\nYou correctly answered the question in {timeTakenToAnswer} seconds! You deal {character.attack} damage!')
            print("Good job, but he is still alive! Answer the next question correctly to finish him!")

            question = getQuestion(mediumQuestions) # Gets second question randomly from dictionary
            answer = getAnswer(mediumQuestions, question) # Gets answer based on initial dictionary/key
            answerIndex = whereInsertRealAnswer() # Stores where the answer was inserted in answer choices list
            answerChoices = getAnswerChoices(answerIndex, answer, incompleteAnswerList) # Gives list of answer choices w the real answer inserted randomly

            print(question) # Prints question
            print(f'\n   A) {answerChoices[0]}\n   B) {answerChoices[1]}\n   C) {answerChoices[2]}\n   D) {answerChoices[3]}\n') # Prints answer choices
            startTime = time.time() # Start timer
            playerAnswer = input() # Takes answer input

            while True:

                if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                    break
                else:
                    playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

            endTime = time.time() # End timer

            timeTakenToAnswer = getElapsedTime(startTime, endTime) # Calculate elapsed time
            completionTime += timeTakenToAnswer
            time.sleep(2)

# \/ Check if second answer was correct \/

            if calculateCritical(character.critTime, timeTakenToAnswer) == True:
                print(f'\nYou correctly answered the question and defeated the enemy! Way to go!')

            else:
                print("\nOh no! Your answer was incorrect! Try one more time...if you get it wrong, you will be defeated!")
                
                playerAnswer = input()

                while True:

                    if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                        break
                    else:
                        playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

                if isCorrect(playerAnswer) == True: # Player deals half damage if correct on the second try
                    print(f"\nYou did it! {character.attack} damage was dealt and you avoided taking damage.")

                else: # Player dies if incorrect on the second try
                    print("\nOh no! You were defeated! Better luck next time...")
                    quit()

    else:
        print("\nOh no! Your answer was incorrect! Try one more time...if you get it wrong, you will be defeated!")
        playerAnswer = input() # Takes answer input

        while True:

            if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                break
            else:
                playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")
        
        if isCorrect(playerAnswer) == True: # Player deals half damage if correct on the second try
            print(f"\nYou did it! {character.attack} damage was dealt and you avoided taking damage.")

        else: # Player dies if incorrect on the second try
            print("\nOh no! You were defeated! Better luck next time...")
            quit()

# \/ Fourth post-combat text, only display this + following if player wins battle(?) \/


    print("You pant heavily, out of breath. Ernulf falls to one knee, unable to stand after taking so much damage.\n")
    time.sleep(6)
    print('“Where is she?” You growl, your arm raised, ready to strike again if Ernulf is still uncooperative.\n')
    time.sleep(6)
    print('Ernulf sighs, resigned. “Your sister is as good as dead… The wicked mage Morden the Grim has her."\n\n\n')
    time.sleep(6)

    print("This information hits you like a boulder launched by a catapult.\n")
    time.sleep(4)
    print("Morden the Grim?\n")
    time.sleep(4)
    print("You knew who that was-everyone did. He had terrorized these lands for decades.\n")
    time.sleep(6)
    print("It was said that any who ended up in his clutches would suffer a fate worse than death. That incarnation of evil was the one who had your sister?\n")
    time.sleep(8)
    print('“He hired us to gather people for him,” Ernulf spat. He was clearly not happy to have worked with Morden.\n')
    time.sleep(5)
    print('“Do you see now why I say that this path only leads to your death? If you want to live, go back now.”\n\n')
    time.sleep(6)
    print("For a second, you consider his words. After all, what could you do against the most powerful mage in the world?\n")
    time.sleep(6)
    print("Even the strongest knights and heroes in the kingdom had failed to put an end to his tyranny.\n")
    time.sleep(5)
    print("Maybe it really would be best for you to go home…\n")
    time.sleep(3)

    print(".\n")
    time.sleep(2)
    print(".\n")
    time.sleep(2)
    print(".\n\n")

    print("No.\n")
    time.sleep(5)
    print("You had already come this far, and you were not going to leave your sister in the hands of someone like Morden.\n")
    time.sleep(8)
    print("With your mind made up and your resolve hardened, you look Ernulf in the eye.\n")
    time.sleep(5)
    print('Tell me where Morden is,” you say. Ernulf is surprised, and looks at you with a mixture of disbelief and something akin to respect.\n') 
    time.sleep(6)
    print('“If that is your choice…” He begins. “He has set up a lair on the tallest mountain, directly east from here.”\n')
    time.sleep(5)
    print("As soon as the words leave his mouth, you turn around and run out of the shelter. You don\'t even bother sneaking past the bandits, instead sprinting straight to the gap in the fence.\n")
    time.sleep(10)
    print("The bandits are surprised to see you, and some of them start yelling at each other to go after you.\n")
    time.sleep(7)
    print("Once you make it to the gap in the fence, you look back and expect to see them behind you. For some reason, however, they have not followed you.\n")
    time.sleep(9)
    print("You are not sure why, but you do not care. You continue running, heading east.\n\n\n\n")
    time.sleep(3)

    print(".\n")
    time.sleep(2)
    print(".\n")
    time.sleep(2)
    print(".\n\n")
    time.sleep(2)


# \/ End part 2 \/

# \/ Part 3/3, Finale \/

# \/ Transition Text 4 \/


    print("You can see the mountain in the distance.\n")
    time.sleep(5)
    print("It is incredibly tall, towering over the other peaks in the vicinity.\n")
    time.sleep(5)
    print("As you draw closer to it, you feel a sense of foreboding. It is as if you can instinctually tell that something dangerous lies within that mountain.\n")
    time.sleep(9)
    print("The feeling only intensifies the nearer you get, until you are finally standing at the base of the mountain.\n")
    time.sleep(7)
    print("As you look up the seemingly never ending slopes, a deep and overwhelming feeling of dread washes over you.\n")
    time.sleep(7)
    print("Every fiber of your being screams at you to run as far away as you possibly can.\n")
    time.sleep(6)
    print("You remind yourself of why you have come this far and press on.\n\n")
    time.sleep(5)
    print("You begin to climb the mountain. You do not know exactly where you need to go, but you feel like you will somehow make it there.\n")
    time.sleep(8)
    print("After walking for what felt like hours but in reality was just a few minutes, you notice something on the side of the mountain.\n")
    time.sleep(8)
    print("You move closer to investigate and realize that it is a small cave opening. The feeling of dread suddenly intensifies as you stand at the opening and you realize that this is where Morden must be.\n\n\n")
    time.sleep(10)
    print("This is where your sister is.\n\n\n")
    time.sleep(5)
    print("You take a deep breath and enter the cave.\n")
    time.sleep(3)
    
    print(".\n")
    time.sleep(2)
    print(".\n")
    time.sleep(2)
    print(".\n\n")
    time.sleep(2)

    print("As soon as you step through the narrow opening, the atmosphere seems to change. Even though you are still near the entrance, there seems to be next to no light.\n")
    time.sleep(7)
    print("You can barely see, and you can feel that the lack of light is not natural.\n")
    time.sleep(5)
    print("You find breathing to be more difficult, as if you are being smothered by the unnatural darkness.\n")
    time.sleep(5)
    print("Still, you press on, running your hand along the wall to guide yourself forward.\n\n")
    time.sleep(5)

    print("You stumble forward through the darkness, doing your best to avoid tripping over the uneven floor.\n")
    time.sleep(5)
    print("With every step you take, the unnatural feeling of dread you feel intensifies. This only assures you that you are going the right way.\n\n")
    time.sleep(7)

    print("Eventually, the tunnel opens up into a larger cavern. A bright light shines from somewhere in the room.\n")
    time.sleep(5)
    print("You are briefly blinded by the light, your eyes having gotten used to the previous darkness.\n")
    time.sleep(5)
    print("After a moment, your eyes adjust to the light.\n")
    time.sleep(5)
    print("In the middle of the room, you can make out a figure lying on the ground.\n")
    time.sleep(5)
    print("You cautiously step forward to investigate, your guard up. As you get closer, you realize that you recognize this figure.\n")
    time.sleep(8)
    print("Your eyes widen as your breath catches in your throat. You sprint the remaining distance, your heart pounding in your chest.\n")
    time.sleep(5)
    print("You kneel next to the unconscious figure of your sibling.\n")
    time.sleep(5)
    print("She is still breathing, but you can tell that she will not last much longer.\n")
    time.sleep(6)
    print("You are about to pick her up, but before you can, a voice rings out from behind you.\n\n")
    time.sleep(6)
    print('“Was (he/she) someone you knew?” The voice says. It is not loud, yet it seems to reverberate through your head.\n')
    time.sleep(7)
    print("You spin around, your heartbeat at an all-time high. As you lay eyes on the person who spoke, you instinctively know who it is.\n")
    time.sleep(5)
    print("He seems impossibly old and frail, as if he could crumble to dust at any moment. At the same time, however, he seems to stand firm, as if he is in perfectly good health.\n")
    time.sleep(7)
    print("His eyes seem to pierce right through you, staring directly into your soul.\n")
    time.sleep(5)
    print('“You should not have come here,” the man says.\n')
    time.sleep(5)
    print("Suddenly, a deep rumbling echoes throughout the cave. The entire cavern begins to shake.\n")
    time.sleep(6)
    print("The floor begins to crack, and you realize that something is rising up through it.\n")
    time.sleep(6)
    print("You jump back as something massive breaks through the floor and then keeps rising, breaking through the ceiling as well.\n")
    time.sleep(7)
    print("You pick up your sister and jump backwards as parts of the ceiling come crashing down on the spot where you had just been standing.\n")
    time.sleep(7)
    print("You look up through the new opening where the cavern\'s ceiling once was, seeing a massive dragon flying in the air above you. On its back stands Morden, looking down at you.\n")
    time.sleep(7)
    print('“You have walked into your death, child, and I am glad that you have. My previous experiments were all failures. It makes me happy to have another chance.” Morden says.\n')
    time.sleep(7)
    print("You put your sister down gently, knowing that you must fight, or both of you will die.\n\n\n\n")
    time.sleep(6)

# \/ Fifth Combat \/

    print('\nTo attack, answer the given question correctly.')
    time.sleep(4)
    print(f'\nTo slay him in one hit, answer the question within {character.critTime} seconds. Ready?\n')
    time.sleep(4)
            
    question = getQuestion(hardQuestions) # Gets question randomly from dictionary
    answer = getAnswer(hardQuestions, question) # Gets answer based on initial dictionary/key
    answerIndex = whereInsertRealAnswer() # Stores where the answer was inserted in answer choices list
    answerChoices = getAnswerChoices(answerIndex, answer, incompleteAnswerList) # Gives list of answer choices w the real answer inserted randomly

    print(question) # Prints question
    print(f'\n   A) {answerChoices[0]}\n   B) {answerChoices[1]}\n   C) {answerChoices[2]}\n   D) {answerChoices[3]}\n\n') # Prints answer choices
    startTime = time.time() # Start timer
    
    playerAnswer = input() # Takes answer input
    
    while True:

        if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
            break
        else:
            playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

    endTime = time.time() # End timer

    timeTakenToAnswer = getElapsedTime(startTime, endTime) # Calculate elapsed time
    completionTime += timeTakenToAnswer
    time.sleep(2)
 
# \/ Checks if answer was true; if so, critical hit? \/

    if isCorrect(playerAnswer) == True:
        if calculateCritical(character.critTime, timeTakenToAnswer) == True:
            print(f'\nYou correctly answered the question in {timeTakenToAnswer} seconds! That\'s a CRITICAL HIT! ')

# \/ If non-lethal was dealt, asks another question so you can deal full damage \/

        else: 
            print(f'\nYou correctly answered the question in {timeTakenToAnswer} seconds! You deal {character.attack} damage!')

            question = getQuestion(hardQuestions) # Gets second question randomly from dictionary
            answer = getAnswer(hardQuestions, question) # Gets answer based on initial dictionary/key
            answerIndex = whereInsertRealAnswer() # Stores where the answer was inserted in answer choices list
            answerChoices = getAnswerChoices(answerIndex, answer, incompleteAnswerList) # Gives list of answer choices w the real answer inserted randomly

            print(question) # Prints question
            print(f'\n   A) {answerChoices[0]}\n   B) {answerChoices[1]}\n   C) {answerChoices[2]}\n   D) {answerChoices[3]}\n') # Prints answer choices
            startTime = time.time() # Start timer
            playerAnswer = input() # Takes answer input

            while True:

                if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                    break
                else:
                    playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

            endTime = time.time() # End timer

            timeTakenToAnswer = getElapsedTime(startTime, endTime) # Calculate elapsed time
            completionTime += timeTakenToAnswer
            time.sleep(2)

# \/ Check if second answer was correct \/

            if calculateCritical(character.critTime, timeTakenToAnswer) == True:
                print(f'\nYou correctly answered the question! Way to go!')

            else:
                print("\nOh no! Your answer was incorrect! Try one more time...if you get it wrong, you will be defeated!")
                
                playerAnswer = input()

                while True:

                    if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                        break
                    else:
                        playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

                if isCorrect(playerAnswer) == True: # Player deals half damage if correct on the second try
                    print(f"\nYou did it! {character.attack} damage was dealt and you avoided taking damage.")

                else: # Player dies if incorrect on the second try
                    print("\nOh no! You were defeated! Better luck next time...")
                    quit()

    else:
        print("\nOh no! Your answer was incorrect! Try one more time...if you get it wrong, you will be defeated!")
        playerAnswer = input() # Takes answer input

        while True:

            if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                break
            else:
                playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")
        
        if isCorrect(playerAnswer) == True: # Player deals half damage if correct on the second try
            print(f"\nYou did it! {character.attack} damage was dealt and you avoided taking damage.")

        else: # Player dies if incorrect on the second try
            print("\nOh no! You were defeated! Better luck next time...")
            quit()

# ------------------------------------------------------------------Asks another series of questions------------------------------------------------------------------------

    question = getQuestion(hardQuestions) # Gets question randomly from dictionary
    answer = getAnswer(hardQuestions, question) # Gets answer based on initial dictionary/key
    answerIndex = whereInsertRealAnswer() # Stores where the answer was inserted in answer choices list
    answerChoices = getAnswerChoices(answerIndex, answer, incompleteAnswerList) # Gives list of answer choices w the real answer inserted randomly

    print(question) # Prints question
    print(f'\n   A) {answerChoices[0]}\n   B) {answerChoices[1]}\n   C) {answerChoices[2]}\n   D) {answerChoices[3]}\n\n') # Prints answer choices
    startTime = time.time() # Start timer
    
    playerAnswer = input() # Takes answer input
    
    while True:

        if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
            break
        else:
            playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

    endTime = time.time() # End timer

    timeTakenToAnswer = getElapsedTime(startTime, endTime) # Calculate elapsed time
    completionTime += timeTakenToAnswer
    time.sleep(2)
 
# \/ Checks if answer was true; if so, critical hit? \/

    if isCorrect(playerAnswer) == True:
        if calculateCritical(character.critTime, timeTakenToAnswer) == True:
            print(f'\nYou correctly answered the question in {timeTakenToAnswer} seconds! That\'s a CRITICAL HIT! ')

# \/ If non-lethal was dealt, asks another question so you can deal full damage \/

        else: 
            print(f'\nYou correctly answered the question in {timeTakenToAnswer} seconds! You deal {character.attack} damage!')

            question = getQuestion(hardQuestions) # Gets second question randomly from dictionary
            answer = getAnswer(hardQuestions, question) # Gets answer based on initial dictionary/key
            answerIndex = whereInsertRealAnswer() # Stores where the answer was inserted in answer choices list
            answerChoices = getAnswerChoices(answerIndex, answer, incompleteAnswerList) # Gives list of answer choices w the real answer inserted randomly

            print(question) # Prints question
            print(f'\n   A) {answerChoices[0]}\n   B) {answerChoices[1]}\n   C) {answerChoices[2]}\n   D) {answerChoices[3]}\n') # Prints answer choices
            startTime = time.time() # Start timer
            playerAnswer = input() # Takes answer input

            while True:

                if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                    break
                else:
                    playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

            endTime = time.time() # End timer

            timeTakenToAnswer = getElapsedTime(startTime, endTime) # Calculate elapsed time
            completionTime += timeTakenToAnswer
            time.sleep(2)

# \/ Check if second answer was correct \/

            if calculateCritical(character.critTime, timeTakenToAnswer) == True:
                print(f'\nYou correctly answered the question! Way to go!')

            else:
                print("\nOh no! Your answer was incorrect! Try one more time...if you get it wrong, you will be defeated!")
                
                playerAnswer = input()

                while True:

                    if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                        break
                    else:
                        playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

                if isCorrect(playerAnswer) == True: # Player deals half damage if correct on the second try
                    print(f"\nYou did it! {character.attack} damage was dealt and you avoided taking damage.")

                else: # Player dies if incorrect on the second try
                    print("\nOh no! You were defeated! Better luck next time...")
                    quit()

    else:
        print("\nOh no! Your answer was incorrect! Try one more time...if you get it wrong, you will be defeated!")
        playerAnswer = input() # Takes answer input

        while True:

            if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                break
            else:
                playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")
        
        if isCorrect(playerAnswer) == True: # Player deals half damage if correct on the second try
            print(f"\nYou did it! {character.attack} damage was dealt and you avoided taking damage.")

        else: # Player dies if incorrect on the second try
            print("\nOh no! You were defeated! Better luck next time...")
            quit()

# ------------------------------------------------------------------Asks another series of questions------------------------------------------------------------------------

    question = getQuestion(hardQuestions) # Gets question randomly from dictionary
    answer = getAnswer(hardQuestions, question) # Gets answer based on initial dictionary/key
    answerIndex = whereInsertRealAnswer() # Stores where the answer was inserted in answer choices list
    answerChoices = getAnswerChoices(answerIndex, answer, incompleteAnswerList) # Gives list of answer choices w the real answer inserted randomly

    print(question) # Prints question
    print(f'\n   A) {answerChoices[0]}\n   B) {answerChoices[1]}\n   C) {answerChoices[2]}\n   D) {answerChoices[3]}\n\n') # Prints answer choices
    startTime = time.time() # Start timer
    
    playerAnswer = input() # Takes answer input
    
    while True:

        if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
            break
        else:
            playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

    endTime = time.time() # End timer

    timeTakenToAnswer = getElapsedTime(startTime, endTime) # Calculate elapsed time
    completionTime += timeTakenToAnswer
    time.sleep(2)
 
# \/ Checks if answer was true; if so, critical hit? \/

    if isCorrect(playerAnswer) == True:
        if calculateCritical(character.critTime, timeTakenToAnswer) == True:
            print(f'\nYou correctly answered the question in {timeTakenToAnswer} seconds! That\'s a CRITICAL HIT! ')

# \/ If non-lethal was dealt, asks another question so you can deal full damage \/

        else: 
            print(f'\nYou correctly answered the question in {timeTakenToAnswer} seconds! You deal {character.attack} damage!')

            question = getQuestion(hardQuestions) # Gets second question randomly from dictionary
            answer = getAnswer(hardQuestions, question) # Gets answer based on initial dictionary/key
            answerIndex = whereInsertRealAnswer() # Stores where the answer was inserted in answer choices list
            answerChoices = getAnswerChoices(answerIndex, answer, incompleteAnswerList) # Gives list of answer choices w the real answer inserted randomly

            print(question) # Prints question
            print(f'\n   A) {answerChoices[0]}\n   B) {answerChoices[1]}\n   C) {answerChoices[2]}\n   D) {answerChoices[3]}\n') # Prints answer choices
            startTime = time.time() # Start timer
            playerAnswer = input() # Takes answer input

            while True:

                if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                    break
                else:
                    playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

            endTime = time.time() # End timer

            timeTakenToAnswer = getElapsedTime(startTime, endTime) # Calculate elapsed time
            completionTime += timeTakenToAnswer
            time.sleep(2)

# \/ Check if second answer was correct \/

            if calculateCritical(character.critTime, timeTakenToAnswer) == True:
                print(f'\nYou correctly answered the question! Way to go!')

            else:
                print("\nOh no! Your answer was incorrect! Try one more time...if you get it wrong, you will be defeated!")
                
                playerAnswer = input()

                while True:

                    if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                        break
                    else:
                        playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")

                if isCorrect(playerAnswer) == True: # Player deals half damage if correct on the second try
                    print(f"\nYou did it! {character.attack} damage was dealt and you avoided taking damage.")

                else: # Player dies if incorrect on the second try
                    print("\nOh no! You were defeated! Better luck next time...")
                    quit()

    else:
        print("\nOh no! Your answer was incorrect! Try one more time...if you get it wrong, you will be defeated!")
        playerAnswer = input() # Takes answer input

        while True:

            if playerAnswer.lower() in ['a', 'b', 'c', 'd']:
                break
            else:
                playerAnswer = input("Invalid input. Please enter a valid answer (a, b, c, d).")
        
        if isCorrect(playerAnswer) == True: # Player deals half damage if correct on the second try
            print(f"\nYou did it! {character.attack} damage was dealt and you avoided taking damage.")

        else: # Player dies if incorrect on the second try
            print("\nOh no! You were defeated! Better luck next time...")
            quit()

# \/ Fifth post-combat text \/

    print("The dragon lets out a deafening screech as you deal the final blow. As the dragon struggles to stay airborne, Morden shouts in anger and disbelief.\n")
    time.sleep(9)
    print('“No! How could this be!?” He bellows, his eyes wide and wild.\n')
    time.sleep(5)
    print("The dragon lets out a final weak whimper as, no longer able to maintain flight, it plummets to the ground.\n")
    time.sleep(7)
    print("Morden lets out a final howl of anger and despair, which is abruptly cut off as the dragon crashes into the ground.\n\n\n")
    time.sleep(8)


# \/ First Possible Ending, only display if player completes battles quickly enough \/

    print(completionTime)

    if completionTime <= 30:
        print("You pant, attempting to catch your breath. Somehow, you managed to win.\n")
        time.sleep(5)
        print("With the danger gone, you rush back to your sister.\n")
        time.sleep(5)
        print("You kneel next to her and are relieved to find that she is still breathing. Still, you know that she needs help quickly, or she will not survive.\n")
        time.sleep(8)
        print("Wasting no more time, you pick her up.\n")
        time.sleep(5)
        print("Although you are tired after your journey and the difficult battle, you set out immediately, heading back towards the city.\n")
        time.sleep(7)
        print("As you do, you smile to yourself.\n")
        time.sleep(7)
        print("Despite the condition of your sister, you can somehow feel that she will be okay.\n")
        quit()

    else:

        print("You pant, attempting to catch your breath. Somehow, you managed to win.\n")
        time.sleep(6)
        print("With the danger gone, you rush back to your sister.\n")
        time.sleep(5)
        print("You kneel next to her, placing your ear against her chest.\n")
        time.sleep(5)
        print("Your heart drops as you realize that you cannot hear any breathing.\n")
        time.sleep(6)
        print("A new fear washes over you, greater than anything else you have felt so far. You pull your head away and look down at her.\n")
        time.sleep(8)
        print("You frantically scan her body, searching for any signs of life.\n\n\n")
        time.sleep(8)
        print("There are none.\n")
        time.sleep(8)
        print("Your body trembles as you look at her face.\n")
        time.sleep(5)
        print("She still looks so normal, as if she could open her eyes at any moment.\n\n")
        time.sleep(6)
        print("You know that won\'t happen, however.\n\n")
        time.sleep(5)
        print("Deep down, you know that she is already dead.\n")
        time.sleep(7)
        print("A wave of emotions washes over you, filling you a volatile mixture of anger and sadness.")
        time.sleep(7)
        print("You throw back your head as a roar of pain and grief bursts out from deep within you, only stopping once you are out of breath.")
        time.sleep(8)
        print("Your body stops trembling as you suddenly feel empty, and you realize that you are alone.")
        quit()
    
