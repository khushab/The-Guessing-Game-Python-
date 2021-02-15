import random

randNumber = random.randint(1, 100)
print(randNumber)
guesses = 0
userGuess = None

while(userGuess != randNumber):

    userGuess = int(input("Enter you guess(between 1 to 100): \n"))
    if(userGuess == randNumber):
        print("Congratulations!! You guessed it right")
    elif(userGuess < randNumber):
        print("You guessed it wrong, please enter a HIGHER NUMBER")
    elif(userGuess > randNumber):
        print("You guessed it wrong, please enter a LOWER NUMBER")
    else:
        print("Invalid input!!")

    guesses = guesses + 1

print(f"You guessed it in {guesses} guesses")

with open("highscore.txt", 'r') as f:
    highscore = f.read()
    if(highscore == ""):
        highscore = 0
    else:
        highscore = int(highscore)

if(guesses < highscore or highscore == 0):
    print("You have broken the highscore!!")
    with open("highscore.txt", 'w') as f:
        f.write(str(guesses))
