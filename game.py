import random
def rpsGame():
    moves = ['rock','paper','scissors']
    gameText = """
    Welcome to Rock Paper Scissors!\n 
    ============================\n 
    You will play against the computer, note this ain't rigged!\n 
    ============================\n 
    Now, type rock paper or scissors\n
    """
    userInput = str(input(gameText))
    rand = random.choice(moves)
    print("\n   Computer chose: ", rand,"\n")
    result = 0
    if (userInput == 'rock' or userInput == 'paper' or userInput == 'scissors' or userInput == 'r' or userInput == 'p' or userInput == 's'):
        #result = 1 (draw) = 0 (lose) = 2(win)
        if userInput == 'rock' or userInput == 'r':
            if rand == 'rock':
                result = 1
            elif rand == 'paper':
                result = 0
            elif rand == 'scissors':
                result = 2
        elif userInput == 'paper' or userInput == 'p':
            if rand == 'rock':
                result = 2
            elif rand == 'paper':
                result = 1
            elif rand == 'scissors':
                result = 0
        elif userInput == 'scissors' or userInput == 's':
            if rand == 'rock':
                result = 0
            elif rand == 'paper':
                result = 2
            elif rand == 'scissors':
                result = 1
        if result == 2:
            print("   You Won") 
        elif result == 1:
            print("   Draw!")
        elif result == 0:
            print("   You lose!")
        result = 0
        playAgn()
    else:
        print("Error with input detected, try again \n\n")
        rpsGame()

def playAgn():
        playAgain = str(input("\n   Want to play again? y/n \n\n"))
        if playAgain == 'y':
            rpsGame()
        elif playAgain == 'n':
            exit()
        else:
            print("Error with input, try again")
            playAgn()
rpsGame()                  

